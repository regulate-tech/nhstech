import pandas as pd
from datetime import timedelta

from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
    ValueType, # We still need this for the Entity
)
# --- THE FIX IS HERE ---
# We import the specific type classes
from feast.types import Bool, Float32, Int64 

# --- 1. Define Data Source ---
patient_gp_data_source = FileSource(
    name="patient_gp_data_source",
    path="data/patient_gp_data.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# --- 2. Define Entity ---
# ValueType is used correctly here
patient = Entity(
    name="patient_id", 
    value_type=ValueType.INT64, 
    description="Unique patient identifier"
)

# --- 3. Define the Feature View ---
gp_records_view = FeatureView(
    name="gp_records",
    entities=[patient],
    ttl=timedelta(days=365 * 10),
    schema=[
        # --- AND THE FIX IS HERE ---
        # We use the imported type classes
        Field(name="patient_age_years", dtype=Int64),
        Field(name="patient_bmi_latest", dtype=Float32),
        Field(name="patient_systolic_bp_avg_12months", dtype=Float32),
        Field(name="patient_has_hypertension", dtype=Bool),
        Field(name="patient_family_history_diabetes", dtype=Bool),
    ],
    online=True,
    source=patient_gp_data_source,
    tags={"owner": "clinical_data_team"},
)