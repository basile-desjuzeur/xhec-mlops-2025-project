import logging
from typing import List

import numpy as np
import pandas as pd
from lib.models import AbaloneInput
from sklearn.base import BaseEstimator
from skrub import TableVectorizer

logger = logging.getLogger(__name__)

CATEGORICAL_COLS = ["Sex"]


def run_inference(input_data: List[AbaloneInput], dv: TableVectorizer, model: BaseEstimator) -> np.ndarray:
    """Run inference on a list of Abalone input data.

    Args:
        input_data (List[AbaloneInput]): list of Pydantic input objects.
        dv: preprocessor (DictVectorizer, ColumnTransformer, etc.)
        model: pickled ML model (already fitted)

    Returns:
        np.ndarray: predicted number of Rings
    """
    logger.info(f"Running inference on input data:\n{input_data}")

    # Convert Pydantic objects to DataFrame
    df = pd.DataFrame([x.dict() for x in input_data])

    # Encoder les colonnes catégorielles
    dicts = df[CATEGORICAL_COLS].to_dict(orient="records")
    X_cat = dv.transform(dicts)

    # Ajouter les colonnes numériques
    numeric_cols = [col for col in df.columns if col not in CATEGORICAL_COLS]
    X_num = df[numeric_cols].to_numpy()

    # Combiner
    X = np.hstack([X_num, X_cat])

    # Prédiction
    y = model.predict(X)
    logger.info(f"Predicted Abalone Rings:\n{y}")
    return y
