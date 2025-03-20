# Description: Pydantic models for the Scout Activities API

from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class Group(str, Enum):
    louveteaux = "louveteaux"
    louvettes = "louvettes"
    lionceaux = "lionceaux"
    lioncelles = "lioncelles"
    eclaireurs = "eclaireurs"
    eclaireuses = "eclaireuses"
    partisans = "partisans"
    partisanes = "partisanes"

class Activity(BaseModel):
    name: str
    groups: List[Group]
    description: Optional[str] = None