from app import app
from flask import render_template, request
from app.models.events_list import events, add_new_event
from app.models.event import *

@app.route('/')
def index():
    #call render_template and give it the name of the file you want it to render and any variables you want it to use
    return render_template('index.html', title='home', tasks=tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_desc = request.form['description']
    new_task = Task(task_title, task_desc, False)
    add_new_task(new_task)
    return render_template('index.html', title='Home', tasks=tasks)