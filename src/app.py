from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In-memory activity database
activities = {
   "Chess Club": {
      "description": "Learn strategies and compete in chess tournaments",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Programming Class": {
      "description": "Learn programming fundamentals and build software projects",
      "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Gym Class": {
      "description": "Physical education and sports activities",
      "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   "Basketball Team": {
      "description": "Competitive basketball training and games",
      "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 15,
      "participants": []
   }
}

@app.get("/activities")
def get_activities():
    return activities

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
   """Sign up a student for an activity"""
   # Validate activity exists
   if activity_name not in activities:
      raise HTTPException(status_code=404, detail="Activity not found")

   # Get the activity
   activity = activities[activity_name]

   # Validate student is not already signed up
   if email in activity["participants"]:
     raise HTTPException(status_code=400, detail="Student is already signed up")

   # Add student
   activity["participants"].append(email)
   return {"message": f"Signed up {email} for {activity_name}"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
