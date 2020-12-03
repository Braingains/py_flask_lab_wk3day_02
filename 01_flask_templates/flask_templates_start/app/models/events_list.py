from app.models.event import *



event1 = Event("3/10/2020", "EventLab", 2, "GreenRoom", "MentalExercise")
event2 = Event("26/1/2021", "21st Birthday", 20, "Deluxe Room", "Celebration")
events = [event1, event2]


def add_new_event(event):
    events.append(event)
