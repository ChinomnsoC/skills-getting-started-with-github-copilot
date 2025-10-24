"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
# In-memory activity database (including the additional activities)
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

    # Sports (added)
    "Soccer Team": {
        "description": "Join the interscholastic soccer team for training and matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Lap swimming, stroke clinics, and friendly competitions",
        "schedule": "Mondays and Wednesdays, 5:00 PM - 6:30 PM",
        "max_participants": 30,
        "participants": ["noah@mergington.edu"]
    },

    # Artistic (added)
    "Art Studio": {
        "description": "Open studio for painting, drawing, and mixed media projects",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "mia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, stagecraft, and production of one play per term",
        "schedule": "Fridays, 3:30 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["lucas@mergington.edu"]
    },

    # Intellectual (added)
    "Robotics Club": {
        "description": "Design and build robots for challenges and competitions",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 16,
        "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Practice public speaking, research, and participate in debate tournaments",
        "schedule": "Mondays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["oliver@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
