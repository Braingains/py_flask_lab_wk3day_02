from app.models.event import *



event1 = Event("EventLab", "MentalExercise")
event2 = Event("21st Birthday", "Celebration")
events = [event1, event2]


def add_new_event(event):
    events.append(event)
