from flask import json
from refla import db, app as refla
#from refla import tasks

testtasks = [{'id':1, 'title': 'test'}]

class TestTasks:
	
	def setup(self):
		refla.app.config['TESTING'] = True
		self.app = refla.app.test_client()

	def test_get_tasks(self):
		db.data = testtasks
		response = self.app.get('/api/tasks')
		assert response.status_code == 200
		assert response.data == json.dumps({'tasks': testtasks}, indent=2)
