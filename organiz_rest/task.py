"""
This is the task module and supports all the ReST actions for the
TASK collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
TASK = [
  { 'id': 0, 'name': 'Init front' },
  { 'id': 1, 'name': 'Make back-end' },
  { 'id': 2, 'name': 'Try deploy localy' },
  { 'id': 3, 'name': 'Try deploy to Internet' },
  { 'id': 4, 'name': 'Add authentication' },
  { 'id': 5, 'name': 'Add features' },
  { 'id': 6, 'name': 'Try using OVH' },
  { 'id': 7, 'name': 'Let`s go to prod :)' },
  { 'id': 8, 'name': 'Test user experience' },
  { 'id': 9, 'name': '...' }
]


def read_all():
    """
    This function responds to a request for /api/task
    with the complete lists of task
    :return:        json string of list of task
    """
    # Create the list of task from our data
    return TASK


def read_one(id):
    """
    This function responds to a request for /api/task/{id}
    with one matching task from task
    :param id:   id of task to find
    :return:        task matching id
    """
    # Does the task exist in task?
    if id < len(TASK):
        task = TASK[id]

    # otherwise, nope, not found
    else:
        abort(
            404, "Task with last name {id} not found".format(id=id)
        )

    return task


def create(task):
    """
    This function creates a new task in the task structure
    based on the passed in task data
    :param task:  task to create in task structure
    :return:        201 on success, 406 on task exists
    """
    id = len(TASK)
    name = task.get("name", None)

    # Does the task exist already?
    task = {
        "id": id,
        "name": name
    }
    TASK.append(task)

    return task


def update(task):
    """
    This function updates an existing task in the task structure
    :param id:   last name of task to update in the task structure
    :param task: task to update
    :return:     updated task structure
    """
    # Does the task exist in task?
    id = task.get('id')
    if id < len(TASK):
        TASK[id]["name"] = task.get("name")
        TASK[id]["timestamp"] = get_timestamp()

        return TASK[id]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Task with last name {id} not found".format(id=id)
        )


def delete(id):
    """
    This function deletes a task from the task structure
    :param id:   last name of task to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the task to delete exist?
    if id < len(TASK):
        del TASK[id]
        return make_response(
            "{id} successfully deleted".format(id=id), 200
        )

    # Otherwise, nope, task to delete not found
    else:
        abort(
            404, "Task with last name {id} not found".format(id=id)
        )

