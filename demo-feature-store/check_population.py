import pandas as pd
import joblib
from feast import FeatureStore
import os
import sys

# --- Configuration ---
# Ensure these match your app.py and lib.py settings
MODEL_FILE = "diabetes_model.pkl"
FEATURES_FILE = "feature_list.pkl"
FEAST_REPO_PATH = "nhs_risk_calculator"
DATA_FILE = "nhs_risk_calculator/data/patient_gp_data.parquet"

# These thresholds MUST match what is in app.py
HIGH_RISK_THRESHOLD = 0.35   # (35%)
MEDIUM_RISK_THRESHOLD = 0.15 # (15%)

def categorize_risk(prob):
    """Assigns a risk category based on probability."""
    if prob >= HIGH_RISK_THRESHOLD:
        return "HIGH"
    elif prob >= MEDIUM_RISK_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

def run_population_check():
    """
    Loads all patients from the feature store, runs predictions,
    and prints a summary of the risk distribution.
    """
    print("--- Running Population Risk Analysis ---")
    
    # --- 1. Load Model and Features ---
    try:
        print(f"Loading model from {MODEL_FILE}...")
        model = joblib.load(MODEL_FILE)
        feature_list = joblib.load(FEATURES_FILE)
        feast_features = [f"gp_records:{name}" for name in feature_list]
    except FileNotFoundError:
        print(f"ERROR: Model or feature file not found.", file=sys.stderr)
        print("Please run 'Retrain Risk Model' first.", file=sys.stderr)
        return

    # --- 2. Connect to Feast and Get All Patient IDs ---
    try:
        print("Connecting to feature store...")
        store = FeatureStore(repo_path=FEAST_REPO_PATH)
        
        print(f"Reading patient list from {DATA_FILE}...")
        patient_data = pd.read_parquet(DATA_FILE)
        patient_ids = patient_data['patient_id'].unique()
        
        if len(patient_ids) == 0:
            print("No patients found in data file.")
            return
            
        print(f"Found {len(patient_ids)} unique patients.")
        # Create the entity_rows structure Feast expects
        entity_rows = [{"patient_id": int(pid)} for pid in patient_ids]
        
    except Exception as e:
        print(f"Error connecting to store or reading data: {e}", file=sys.stderr)
        return

    # --- 3. Get Online Features for ALL Patients ---
    try:
        print("Retrieving online features for all patients...")
        online_features_dict = store.get_online_features(
            features=feast_features,
            entity_rows=entity_rows
        ).to_dict()
        
        features_df = pd.DataFrame(online_features_dict)
        # Drop any patients Feast couldn't find (should be 0)
        features_df = features_df.dropna(subset=['patient_id'])
        
    except Exception as e:
        print(f"Error getting online features: {e}", file=sys.stderr)
        return

    # --- 4. Prepare Data and Handle Missing Values ---
    
    # Get just the feature columns in the correct order
    X_predict = features_df[feature_list]
    total_patients = len(X_predict)
    
    # Find rows with ANY null (missing) features
    missing_data_mask = X_predict.isnull().any(axis=1)
    num_missing = missing_data_mask.sum()
    
    # Create a clean DataFrame with only complete records
    X_complete = X_predict[~missing_data_mask]
    
    print(f"\nRetrieved features for {total_patients} patients.")
    print(f"  - {len(X_complete)} patients have complete data.")
    print(f"  - {num_missing} patients have missing data (will be excluded).")
    
    if len(X_complete) == 0:
        print("\nNo patients with complete data. Cannot generate report.")
        return

    # --- 5. Run Predictions and Categorize ---
    print(f"Running predictions on {len(X_complete)} patients...")
    
    # Get the probability of "True" (diabetes)
    probabilities = model.predict_proba(X_complete)[:, 1]
    
    # Assign categories
    risk_groups = [categorize_risk(p) for p in probabilities]
    
    # Count the results
    counts = pd.Series(risk_groups).value_counts()

    # --- 6. Display Report ---
    print("\n--- Population Risk Profile ---")
    print(f"Total Patients Scored: {len(X_complete)}\n")
    print("Risk Group Counts:")
    print("---------------------------------")
    print(f"  HIGH RISK   (>= {HIGH_RISK_THRESHOLD*100: >2.0f}%): \t{counts.get('HIGH', 0)}")
    print(f"  MEDIUM RISK ({MEDIUM_RISK_THRESHOLD*100: >2.0f}-{HIGH_RISK_THRESHOLD*100:2.0f}%): \t{counts.get('MEDIUM', 0)}")
    print(f"  LOW RISK    (< {MEDIUM_RISK_THRESHOLD*100: >2.0f}%): \t{counts.get('LOW', 0)}")
    print("---------------------------------")

if __name__ == "__main__":
    run_population_check()