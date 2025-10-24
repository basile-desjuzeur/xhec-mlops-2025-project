import pandas as pd
from prefect import task
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from skrub import TableVectorizer


@task
def preprocess_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series, TableVectorizer]:
    """Preprocess the input DataFrame and return the features and fitted TableVectorizer."""
    X, y = df.drop(columns=["Rings"]), df[["Rings"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and fit TableVectorizer
    tv = TableVectorizer(numeric=StandardScaler())
    X_train_transformed = tv.fit_transform(X_train, y_train)
    X_test_transformed = tv.transform(X_test)

    return X_train_transformed, y_train, X_test_transformed, y_test, tv
