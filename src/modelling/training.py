import pandas as pd
from prefect import task
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error


@task
def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Train a regression model on the provided training data."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model_on_split(model: LinearRegression, X: pd.DataFrame, y: pd.Series) -> float:
    """Evaluate the model on the provided data and return the RMSE."""
    predictions = model.predict(X)
    rmse = root_mean_squared_error(y, predictions)
    return rmse


@task
def evaluate_model(
    X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series, model: LinearRegression
) -> tuple[float, float]:
    """Evaluate the model on both training and testing data and return the RMSE for each."""
    train_rmse = evaluate_model_on_split(model, X_train, y_train)
    test_rmse = evaluate_model_on_split(model, X_test, y_test)
    return train_rmse, test_rmse
