import pandas as pd
from sklearn.preprocessing import StandardScaler
from skrub import TableVectorizer


def preprocess_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, TableVectorizer]:
    """Preprocess the input DataFrame and return the features and fitted TableVectorizer."""
    X, y = df.drop(columns=["Rings"]), df[["Rings"]]

    # Initialize and fit TableVectorizer
    tv = TableVectorizer(numeric=StandardScaler())
    X_transformed = tv.fit_transform(X)
    return X_transformed, y, tv
