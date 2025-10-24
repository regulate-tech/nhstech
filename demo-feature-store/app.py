
import joblib
import pandas as pd
from flask import Flask, request, render_template, flash, redirect, url_for
from feast import FeatureStore
import os

from lib import (
    generate_and_save_data, 
    run_feast_commands, 
    train_and_save_model,
    MODEL_FILE, 
    FEATURES_FILE, 
    FEAST_REPO_PATH
)

app = Flask(__name__)
app.secret_key = os.urandom(24) 

model = None
feature_list = None
feast_features = []
store = None

def load_resources():
    global model, feature_list, feast_features, store
    
    try:
        model = joblib.load(MODEL_FILE)
        feature_list = joblib.load(FEATURES_FILE)
        feast_features = [f"gp_records:{name}" for name in feature_list]
        print(f"Model and feature list loaded. Features: {feature_list}")
    except FileNotFoundError:
        print("WARNING: Model or feature list not found.")
        print("Please run train_model.py to generate them.")
        model = None
        feature_list = None

    try:
        store = FeatureStore(repo_path=FEAST_REPO_PATH)
        print("Connected to Feast feature store.")
    except Exception as e:
        print(f"FATAL: Could not connect to Feast feature store: {e}")
        store = None


@app.route('/')
def home():
    return render_template('index.html')

# ... (imports, app = Flask(...), load_resources(), home(), etc.) ...

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the form submission and returns a prediction."""
    
    # We define two thresholds to create three levels
    HIGH_RISK_THRESHOLD = 0.35   # (35%)
    MEDIUM_RISK_THRESHOLD = 0.15 # (15%)

    if not model or not store or not feature_list:
        return render_template('index.html', 
                               error="Server error: Model or feature store not loaded.")
    
    patient_id_str = request.form.get('patient_id', '').strip()
    if not patient_id_str.isdigit():
        return render_template('index.html', error="Invalid Patient ID. Must be a number.")

    patient_id = int(patient_id_str)
    
    try:
        entity_rows = [{"patient_id": patient_id}]
        online_features_dict = store.get_online_features(
            features=feast_features,
            entity_rows=entity_rows
        ).to_dict()

        features_df = pd.DataFrame(online_features_dict)
        
        if features_df.empty or features_df['patient_id'][0] is None:
             return render_template('index.html', 
                                    error=f"Patient ID {patient_id} not found.")

        X_predict = features_df[feature_list]
        prediction_error = None

        if X_predict.isnull().values.any():
            prediction_error = "Patient data is incomplete. Prediction may be inaccurate."
            X_predict = X_predict.fillna(0) # Fill with 0 for demo

        
        # 1. Get the probability of "True" (diabetes)
        probability_true = model.predict_proba(X_predict)[0][1]
        
        # 2. Compare against our new thresholds
        if probability_true >= HIGH_RISK_THRESHOLD:
            prediction_text = "HIGH RISK"
        elif probability_true >= MEDIUM_RISK_THRESHOLD:
            prediction_text = "MEDIUM RISK"
        else:
            prediction_text = "LOW RISK"
        
        # 3. Format the results
        risk_percent = round(probability_true * 100, 1)


        return render_template(
            'index.html',
            patient_id=patient_id,
            patient_data=X_predict.to_dict('records')[0],
            prediction=prediction_text,
            probability=risk_percent,
            error=prediction_error
        )

    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

# ... (add_data(), retrain_model(), if __name__ == '__main__':, etc.) ...
@app.route('/add-data', methods=['POST'])
def add_data():
    """Generates new data, materializes it, and reloads the store."""
    global store  
    try:
        generate_and_save_data()
        run_feast_commands()
        
        print("Reloading feature store...")
        store = FeatureStore(repo_path=FEAST_REPO_PATH)
        
        flash("Successfully added 500 new patients and updated feature store.", "success")
    except Exception as e:
        print(f"Error adding data: {e}")
        flash(f"Error adding data: {e}", "error")
        
    return redirect(url_for('home'))


@app.route('/retrain-model', methods=['POST'])
def retrain_model():
    """Retrains the model, saves it, and reloads it into the app."""
    global model, feature_list, feast_features, store 
    
    try:
        train_and_save_model()
        
        model = joblib.load(MODEL_FILE)
        feature_list = joblib.load(FEATURES_FILE)
        feast_features = [f"gp_records:{name}" for name in feature_list]
        
        print("Reloading feature store...")
        store = FeatureStore(repo_path=FEAST_REPO_PATH)

        
        flash("Successfully retrained and reloaded the risk model.", "success")
    except Exception as e:
        print(f"Error retraining model: {e}")
        flash(f"Error retraining model: {e}", "error")
        
    return redirect(url_for('home'))


if __name__ == '__main__':
    load_resources()
    app.run(debug=True)