import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Train a regression model on the provided training data."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
