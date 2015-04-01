from flask import json
from refla import db, app as refla

tasks = [
	{'id':1, 'title': u'test1'},
	{'id':2, 'title': u'test2'}
]

class TestApi:
	
	def setup(self):
		refla.app.config['TESTING'] = True
		self.app = refla.app.test_client()
		db.data = tasks


	def test_get_tasks(self):
		response = self.app.get('/api/tasks')
		assert response.status_code == 200
		assert response.data == json.dumps({'tasks': tasks}, indent=2)


	def test_get_task(self):
		response = self.app.get('/api/tasks/2')
		assert response.status_code == 200
		assert response.data == json.dumps({'task': tasks[1]}, indent=2)


	def test_get_task_not_found(self):
		response = self.app.get('/api/tasks/4711')
		assert response.status_code == 404
		assert response.data == json.dumps({ "message": "404: Not Found" }, indent=2)


	def test_get_task_bad_id(self):
		response = self.app.get('/api/tasks/foul_id')
		assert response.status_code == 404
		assert response.data == json.dumps({ "message": "404: Not Found" }, indent=2)
