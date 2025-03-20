from typing import Optional, List
from fastapi import FastAPI, HTTPException
from models import Activity
from utils import load_activities, save_activities

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
def register_activity(activity: Activity):
    curr_activities = load_activities()
    curr_activities.append(activity)
    save_activities(curr_activities)
    return {"message": "Activity registered successfully"}

@app.get("/search")
def search_activities(name: Optional[str] = None, group: Optional[str] = None) -> List[Activity]:
    curr_activities = load_activities()
    results = [activity for activity in curr_activities if (name is None or name in activity.name) and (group is None or group in activity.groups)]
    if not results:
        raise HTTPException(status_code=404, detail="No activities found")
    return results