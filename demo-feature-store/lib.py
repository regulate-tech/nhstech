
import pandas as pd
import numpy as np  # <-- ADD THIS
import random       # <-- ADD THIS
from faker import Faker
from datetime import datetime, timedelta
import os
import subprocess
import joblib

from feast import FeatureStore
from sklearn.linear_model import LogisticRegression

# --- Configuration (No changes here) ---
DATA_DIR = "nhs_risk_calculator/data"
DATA_FILE = os.path.join(DATA_DIR, "patient_gp_data.parquet")
FEAST_REPO_PATH = "nhs_risk_calculator"
MODEL_FILE = "diabetes_model.pkl"
FEATURES_FILE = "feature_list.pkl"

# --- Data Generation Logic (No changes here) ---

def _create_synthetic_records(num_patients=500, records_per_patient=5):
    """Generates a DataFrame of new synthetic patient data."""
    print(f"Generating data for {num_patients} new patients...")
    
    try:
        existing_df = pd.read_parquet(DATA_FILE)
        start_id = existing_df['patient_id'].max() + 1
    except FileNotFoundError:
        start_id = 1
        
    patient_ids = list(range(start_id, start_id + num_patients))
    all_records = []
    fake = Faker()

    for pid in patient_ids:
        base_age = random.randint(25, 70)
        base_bmi = round(random.uniform(18.0, 40.0), 1)
        base_bp = round(random.uniform(110, 160), 0)
        has_hypertension = (base_bp > 140) or (random.random() < 0.15)
        family_history = random.random() < 0.2
        current_time = datetime.now() - timedelta(days=365 * 2)

        for i in range(records_per_patient):
            event_ts = current_time + timedelta(days=i * 90)
            record_age = base_age + (i * 0.25)
            record_bmi = round(base_bmi + random.uniform(-0.5, 0.5), 1)
            record_bp = round(base_bp + random.uniform(-5, 5), 0)

            all_records.append({
                "patient_id": pid,
                "event_timestamp": event_ts,
                "created_timestamp": datetime.now(), 
                "patient_age_years": int(record_age),
                "patient_bmi_latest": record_bmi,
                "patient_systolic_bp_avg_12months": record_bp,
                "patient_has_hypertension": has_hypertension,
                "patient_family_history_diabetes": family_history,
            })
    
    df = pd.DataFrame(all_records)
    df["patient_age_years"] = df["patient_age_years"].astype(np.int64)
    df["patient_bmi_latest"] = df["patient_bmi_latest"].astype(np.float32)
    df["patient_systolic_bp_avg_12months"] = df["patient_systolic_bp_avg_12months"].astype(np.float32)
    return df

def generate_and_save_data():
    """
    Generates new data and appends it to the existing Parquet file.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    new_data = _create_synthetic_records()
    
    try:
        existing_data = pd.read_parquet(DATA_FILE)
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        print(f"Appending {len(new_data)} new records. Total records: {len(combined_data)}")
    except FileNotFoundError:
        combined_data = new_data
        print(f"Creating new data file with {len(combined_data)} records.")

    combined_data.to_parquet(DATA_FILE, index=False)
    print(f"Data saved to {DATA_FILE}")

def run_feast_commands():
    """Runs 'apply' and 'materialize' to update the feature store."""
    print("Running 'feast apply'...")
    subprocess.run(["feast", "apply"], cwd=FEAST_REPO_PATH, check=True)
    
    print("Running 'feast materialize' (this may take a moment)...")
    
    start_date = "2010-01-01T00:00:00"
    end_date = "2099-01-01T00:00:00"
    
    subprocess.run(
        ["feast", "materialize", start_date, end_date], 
        cwd=FEAST_REPO_PATH, 
        check=True
    )

    print("Feast store updated.")


# --- 2. Model Training Logic  ---

def calculate_diabetes_label(row):
    """
    Calculates a realistic diabetes label based on feature values.
    Returns True (has diabetes) or False (does not).
    """
    # Handle missing data - if any risk factor is missing, return None
    if row.isnull().any():
        return None

    # 1. Start with a base log-odds (e.g., -4.5 is a good test base)
    # This is our 'intercept'
    score = -4.5

    # 2. Add weighted factors (our "correlations")
    
    # Age: Add 0.075 for each year over 40
    score += max(0, row['patient_age_years'] - 40) * 0.075

    # BMI: Add 0.15 for each BMI point over 25 (overweight)
    score += max(0, row['patient_bmi_latest'] - 25) * 0.15

    # Family History: Add a 1.2 "point" bonus (a strong indicator)
    if row['patient_family_history_diabetes']:
        score += 1.2 

    # Hypertension: Add a 0.8 "point" bonus
    if row['patient_has_hypertension']:
        score += 0.8
    
    # 3. Convert log-odds 'score' to probability (0.0 to 1.0)
    # This is the logistic/sigmoid function
    probability = 1 / (1 + np.exp(-score))
    
    # 4. Use this probability to make a weighted random choice
    # If prob is 0.3 (30%), this will return True ~30% of the time.
    return random.random() < probability


def train_and_save_model():
    """
    Fetches latest data from Feast, generates realistic labels, 
    trains a new model, and saves it to disk.
    """
    print("Connecting to Feast store...")
    store = FeatureStore(repo_path=FEAST_REPO_PATH)

    print(f"Reading patient list from {DATA_FILE}...")
    try:
        patient_data = pd.read_parquet(DATA_FILE)
        patient_ids = patient_data['patient_id'].unique()
        if len(patient_ids) == 0:
            raise Exception("No patients found in data file.")
    except FileNotFoundError:
        print("No data file found. Cannot train model.")
        raise Exception("Parquet data file not found. Run 'Add Data' first.")

    print(f"Creating 'entity_df' for {len(patient_ids)} patients...")
    
    # 1. Create the "scaffolding" DataFrame WITHOUT the random label
    entity_df = pd.DataFrame({
        "patient_id": patient_ids,
        "event_timestamp": [
            datetime.now() - timedelta(days=random.randint(365, 365*3)) 
            for _ in patient_ids
        ]
    })
    
    features_to_get = [
        "gp_records:patient_age_years",
        "gp_records:patient_bmi_latest",
        "gp_records:patient_systolic_bp_avg_12months",
        "gp_records:patient_has_hypertension",
        "gp_records:patient_family_history_diabetes",
    ]

    print("Retrieving historical features from Feast...")
    # 2. Get the features for our "scaffolding"
    training_data_job = store.get_historical_features(
        entity_df=entity_df,  # Use the label-less df
        features=features_to_get,
    )
    training_df = training_data_job.to_df()

    print("Calculating realistic diabetes labels based on features...")
    
    # 3. Get the plain feature names (without the 'gp_records:' prefix)
    features = [f.split(":")[1] for f in features_to_get]
    
    # 4. Apply our new realistic logic to create the label
    training_df["developed_diabetes_5yr"] = training_df[features].apply(
        calculate_diabetes_label, 
        axis=1
    )
    
    # Now 'training_df' has features AND a realistic, correlated label
    target = "developed_diabetes_5yr"
    
    print("Cleaning data and training model...")
    # 5. Drop rows where any feature was missing OR our label could not be calculated
    training_df_clean = training_df.dropna(subset=features + [target]).copy()
    
    if training_df_clean.empty:
        print("No complete data rows to train on. Aborting.")
        raise Exception("No complete data rows to train on.")

    X_train = training_df_clean[features]
    y_train = training_df_clean[target]
    print(f"Training on {len(X_train)} complete rows.")

    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("Model training complete.")

    print(f"Saving model to {MODEL_FILE}...")
    joblib.dump(model, MODEL_FILE)
    
    print(f"Saving feature list to {FEATURES_FILE}...")
    joblib.dump(features, FEATURES_FILE)
    print("Model and features saved.")