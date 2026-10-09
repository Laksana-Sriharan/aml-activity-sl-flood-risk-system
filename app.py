import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sri Lanka Flood Predictor", page_icon="🌊")
model = pickle.load(open("model.pkl", "rb"))

CATS = {
    "district": [
        "Ampara",
        "Anuradhapura",
        "Badulla",
        "Batticaloa",
        "Colombo",
        "Galle",
        "Gampaha",
        "Hambantota",
        "Jaffna",
        "Kalutara",
        "Kandy",
        "Kegalle",
        "Kilinochchi",
        "Kurunegala",
        "Mannar",
        "Matale",
        "Matara",
        "Monaragala",
        "Mullaitivu",
        "Nuwara Eliya",
        "Polonnaruwa",
        "Puttalam",
        "Ratnapura",
        "Trincomalee",
        "Vavuniya"
    ],
    "landcover": [
        "Agriculture",
        "Bare Soil",
        "Forest",
        "Plantation",
        "Scrub",
        "Urban",
        "Wetland"
    ],
    "soil_type": [
        "Clay",
        "Loamy",
        "Peaty",
        "Sandy",
        "Silty"
    ],
    "water_supply": [
        "Municipal",
        "Rainwater harvesting",
        "Surface water",
        "Tube-well",
        "Well"
    ],
    "electricity": [
        "Grid",
        "Mixed",
        "Off-grid (solar)"
    ],
    "road_quality": [
        "Fair",
        "Good (paved)",
        "No road access",
        "Poor (unpaved)"
    ],
    "urban_rural": [
        "Rural",
        "Urban"
    ],
    "water_presence_flag": [
        "Likely",
        "Unlikely"
    ]
}

# feature: (min, max, default)
NUMS = {
    "latitude": [
        5.90009,
        9.949978,
        7.9233145
    ],
    "longitude": [
        79.650121,
        81.899993,
        80.760618
    ],
    "elevation_m": [
        0.0,
        2148.0,
        68.0
    ],
    "distance_to_river_m": [
        0.0,
        16802.0,
        1394.2
    ],
    "population_density_per_km2": [
        10.0,
        3113.0,
        519.0
    ],
    "built_up_percent": [
        1.0,
        95.0,
        23.3
    ],
    "rainfall_7d_mm": [
        0.0,
        372.2,
        69.5
    ],
    "monthly_rainfall_mm": [
        0.0,
        863.7,
        202.0
    ],
    "drainage_index": [
        0.003,
        0.999,
        0.501
    ],
    "ndvi": [
        -0.792,
        1.0,
        0.165
    ],
    "ndwi": [
        -1.0,
        1.0,
        0.026
    ],
    "historical_flood_count": [
        0.0,
        5.0,
        0.0
    ],
    "infrastructure_score": [
        5.0,
        95.0,
        46.0
    ],
    "nearest_hospital_km": [
        0.0,
        75.71,
        5.58
    ],
    "nearest_evac_km": [
        0.0,
        55.95,
        4.17
    ]
}

st.title("🌊 Sri Lanka Flood Occurrence Predictor")
st.caption("Enter location details to predict whether a flood is likely.")

values = {}
left, right = st.columns(2)
for i, (name, options) in enumerate(CATS.items()):
    values[name] = (left if i % 2 == 0 else right).selectbox(name, options)
for i, (name, (lo, hi, default)) in enumerate(NUMS.items()):
    is_int = name in ("elevation_m", "population_density_per_km2", "historical_flood_count", "infrastructure_score")
    cast = int if is_int else float
    values[name] = (left if i % 2 == 0 else right).number_input(
        name, min_value=cast(lo), max_value=cast(hi), value=cast(default))

if st.button("Predict", type="primary"):
    prob = model.predict_proba(pd.DataFrame([values]))[0, 1]
    st.progress(float(prob))
    if prob >= 0.5:
        st.error(f"Flood likely — probability {prob:.1%}")
    else:
        st.success(f"Flood unlikely — probability {prob:.1%}")
