# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from pathlib import Path

import pandas as pd
from prefect import flow, get_run_logger
from prefect.artifacts import create_markdown_artifact
from preprocessing import preprocess_data
from training import evaluate_model, train_model
from utils import pickle_object


@flow
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    logger = get_run_logger()
    logger.info(f"Starting training flow with data from: {trainset_path}")

    df = pd.read_csv(trainset_path)
    X_train, y_train, X_test, y_test, tv = preprocess_data(df)
    logger.info("Data preprocessing completed.")

    # (Optional) Pickle encoder if need be
    pickle_object(tv, Path("./web_service/local_objects/table_vectorizer.pkl"))

    # Train model
    model = train_model(X_train, y_train)
    logger.info("Model training completed.")

    # Evaluate model
    rmse_train, rmse_test = evaluate_model(X_train, y_train, X_test, y_test, model)
    create_markdown_artifact(
        key="rmse-train",
        markdown=f"# training rmse: {rmse_train:.4f}",
    )
    create_markdown_artifact(
        key="rmse-test",
        markdown=f"# testing rmse: {rmse_test:.4f}",
    )

    # Pickle model
    pickle_object(model, Path("./web_service/local_objects/regression_model.pkl"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
