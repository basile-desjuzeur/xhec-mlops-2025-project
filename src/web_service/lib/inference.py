import logging
from typing import List

import numpy as np
import pandas as pd
from src.web_service.lib.models import AbaloneInput
from sklearn.base import BaseEstimator
from skrub import TableVectorizer

logger = logging.getLogger(__name__)

CATEGORICAL_COLS = ["Sex"]


def run_inference(
    input_data: List[AbaloneInput], dv: TableVectorizer, model: BaseEstimator
) -> np.ndarray:
    """
    Args:
        input_data (List[AbaloneInput]): list of Pydantic input objects.
        dv: Pre-fitted TableVectorizer from skrub.
        model: pickled ML model (already fitted)

    Returns:
        np.ndarray: predicted number of Rings
    """
    logger.info(f"Running inference on input data:\n{input_data}")

    # 1. Convert Pydantic objects to DataFrame
    # On utilise by_alias=True pour que les clés soient "Whole weight", etc.
    # (en supposant que votre modèle Pydantic utilise des alias)
    df = pd.DataFrame([x.dict(by_alias=True) for x in input_data])

    # 1b. On renomme "Whole weight" en "Whole_weight" (ce que le modèle attend)
    df = df.rename(
        columns={
            "Whole_weight": "Whole weight",
            "Shucked_weight": "Shucked weight",
            "Viscera_weight": "Viscera weight",
            "Shell_weight": "Shell weight",
        }
    )
    logger.info("Colonnes renommées pour correspondre au modèle.")

    # 2. Appliquer le TableVectorizer DIRECTEMENT au DataFrame.
    try:
        X_transformed = dv.transform(df)
    except Exception as e:
        logger.error(f"Erreur pendant dv.transform(df): {e}")
        # On lève l'erreur pour la voir dans la console
        raise e

    # 3. Prédiction
    try:
        y = model.predict(X_transformed)
    except Exception as e:
        logger.error(f"Erreur pendant model.predict(X_transformed): {e}")
        # On lève l'erreur pour la voir dans la console
        raise e

    logger.info(f"Predicted Abalone Rings:\n{y}")
    return y
