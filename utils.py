# Description: This file contains utility functions for the Scout Activities application.

import os
import json
from typing import List
from models import Activity

DATA_FILE = "activities.json"

def load_activities():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Activity(**activity) for activity in data]
    return []

def save_activities(activities: List[Activity]):
    with open(DATA_FILE, "w") as file:
        json.dump([activity.model_dump() for activity in activities], file)