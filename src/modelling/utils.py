import pickle
from pathlib import Path

from prefect import task


@task
def pickle_object(obj: object, path: str) -> None:
    """Pickle the given object to the specified path."""
    with Path.open(path, "wb") as f:
        pickle.dump(obj, f)
