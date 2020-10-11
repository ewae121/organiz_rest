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
TASK = {
  "1": { 'id': 1, 'name': 'Init front' },
  "2": { 'id': 2, 'name': 'Make back-end' },
  "3": { 'id': 3, 'name': 'Try deploy localy' },
  "4": { 'id': 4, 'name': 'Try deploy to Internet' },
  "5": { 'id': 5, 'name': 'Add authentication' },
  "6": { 'id': 6, 'name': 'Add features' },
  "7": { 'id': 7, 'name': 'Try using OVH' },
  "8": { 'id': 8, 'name': 'Let`s go to prod :)' },
  "9": { 'id': 9, 'name': 'Test user experience' },
  "10": { 'id': 10, 'name': '...' }
}


def read_all():
    """
    This function responds to a request for /api/task
    with the complete lists of task
    :return:        json string of list of task
    """
    # Create the list of task from our data
    return [TASK[key] for key in sorted(TASK.keys())]


def read_one(id):
    """
    This function responds to a request for /api/task/{id}
    with one matching task from task
    :param id:   id of task to find
    :return:        task matching id
    """
    # Does the task exist in task?
    if id in TASK:
        task = TASK.get(id)

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
    id = task.get("id", None)
    name = task.get("name", None)

    # Does the task exist already?
    if id not in TASK and id is not None:
        TASK[id] = {
            "id": id,
            "name": name
        }
        return make_response(
            "{id} successfully created".format(id=id), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Task with id {id} already exists".format(id=id),
        )


def update(id, task):
    """
    This function updates an existing task in the task structure
    :param id:   last name of task to update in the task structure
    :param task:  task to update
    :return:        updated task structure
    """
    # Does the task exist in task?
    if id in TASK:
        TASK[id]["fname"] = task.get("fname")
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
    if id in TASK:
        del TASK[id]
        return make_response(
            "{id} successfully deleted".format(id=id), 200
        )

    # Otherwise, nope, task to delete not found
    else:
        abort(
            404, "Task with last name {id} not found".format(id=id)
        )

