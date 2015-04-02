#!flask/bin/python
from flask import Flask, jsonify, abort, request, url_for, render_template
from json_app_factory import create_json_app
import db

app = create_json_app(__name__)


def make_public(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/')
def index():
    return render_template('todo.html')


@app.route('/api')
def api_root():
    return jsonify({'tasks': url_for('get_tasks', _external=True)})


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = db.get_all()
    return jsonify({'tasks': [make_public(task) for task in tasks]})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    return jsonify({'task': make_public(task)})


@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = db.insert({
        'title': request.json['title'],
        'done': False
    })
    return jsonify({'task': make_public(task)}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task = db.update(task_id, {
        'title': request.json.get('title', task['title']),
        'done': request.json.get('done', task['done'])
    })
    return jsonify({'task': make_public(task)})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    db.delete(task_id)
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)