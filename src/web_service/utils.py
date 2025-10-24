import pickle
from pathlib import Path

from sklearn.base import BaseEstimator
from skrub import TableVectorizer


def load_model(path: str) -> BaseEstimator:
    """Load a pickled ML model."""
    with Path.open(path, "rb") as f:
        model = pickle.load(f)
    return model


def load_preprocessor(path: str) -> TableVectorizer:
    """Load a pickled preprocessor (e.g., DictVectorizer)."""
    with Path.open(path, "rb") as f:
        dv = pickle.load(f)
    return dv
