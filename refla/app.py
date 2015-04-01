#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import url_for
from json_flask import make_json_app
import db

app = make_json_app(__name__)

@app.route('/')
def index():
    return 'refla-todo'


@app.route('/api')
def api_root():
    return jsonify({
        'tasks': url_for('get_tasks'),
    })


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = db.get_all()
    return jsonify({'tasks': tasks})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    return jsonify({'task': task})


@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = db.insert({
        'title': request.json['title'],
        'done': False
    })
    return jsonify({'task': task}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    print(task)
    task = db.update(task_id, {
        'title': request.json.get('title', task['title']),
        'done': request.json.get('done', task['done'])
    })
    print(task)
    return jsonify({'task': task})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = db.get(task_id)
    if task is None:
        abort(404)
    db.delete(task_id)
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)