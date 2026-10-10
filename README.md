# Sri Lanka Flood Occurrence Prediction

A machine learning project that predicts flood occurrence in Sri Lanka from geographical, rainfall, and infrastructure features. It compares Random Forest, XGBoost, Soft Voting, and Stacking classifiers on 25,000 records and includes a Streamlit web app for predictions.


| File | Description |
| --- | --- |
| `flood_prediction.ipynb` | Preprocessing, tuning, model comparison, interpretation, inference, and export |
| `model.pkl` | Trained Stacking pipeline (preprocessing + model) |
| `app.py` | Streamlit app for entering features and viewing predictions |
| `sri_lanka_flood_risk_dataset_25000.csv` | Dataset |
| `requirements.txt` | Python dependencies |

## Features

* **Categorical:** `district`, `landcover`, `soil_type`, `water_supply`, `electricity`, `road_quality`, `urban_rural`, `water_presence_flag`
* **Numerical:** `latitude`, `longitude`, `elevation_m`, `distance_to_river_m`, `population_density_per_km2`, `built_up_percent`, `rainfall_7d_mm`, `monthly_rainfall_mm`, `drainage_index`, `ndvi`, `ndwi`, `historical_flood_count`, `infrastructure_score`, `nearest_hospital_km`, `nearest_evac_km`

Leakage columns (`inundation_area_sqm`, `flood_risk_score`, `is_good_to_live`, `reason_not_good_to_live`) are excluded.

## Installation and Usage

```bash
pip install -r requirements.txt
streamlit run app.py
```

If `pip` is not recognised, use `python -m pip install -r requirements.txt` and `python -m streamlit run app.py`.

## Dataset

Sri Lanka Flood Risk & Inundation Dataset. Kaggle. https://www.kaggle.com/datasets/dewminimnaadi/sri-lanka-flood-risk-and-inundation-dataset

## Author

Laksana. S

