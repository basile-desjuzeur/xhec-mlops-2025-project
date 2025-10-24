from app_config import APP_DESCRIPTION, APP_TITLE, APP_VERSION, MODEL_VERSION, PATH_TO_MODEL, PATH_TO_PREPROCESSOR
from fastapi import FastAPI
from lib.modelling.inference import run_inference
from lib.models import AbaloneInput, AbalonePredictionOut
from lib.utils import load_model, load_preprocessor

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)

# Charger modèle et preprocessor une seule fois
dv = load_preprocessor(PATH_TO_PREPROCESSOR)
model = load_model(PATH_TO_MODEL)


@app.get("/")
def home() -> dict:
    """..."""
    return {"health_check": "OK", "model_version": MODEL_VERSION}


@app.post("/predict", response_model=AbalonePredictionOut)
def predict(payload: AbaloneInput) -> dict:
    """..."""
    y = run_inference([payload], dv, model)
    return {"Rings": int(y[0])}
