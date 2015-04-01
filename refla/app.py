#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
import db

app = Flask(__name__)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
	tasks = db.get_all()
	return jsonify({'tasks': tasks})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	tasks = db.get_all()
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
	    abort(404)
	return jsonify({'task': task[0]})



if __name__ == '__main__':
    app.run(debug=True)