# Pydantic models for the web service
from typing import Literal

from pydantic import BaseModel


class AbaloneInput(BaseModel):
    """..."""

    Sex: Literal["M", "F", "I"]
    Length: float
    Diameter: float
    Height: float
    Whole_weight: float
    Shucked_weight: float
    Viscera_weight: float
    Shell_weight: float


class AbalonePredictionOut(BaseModel):
    """..."""

    Rings: int
