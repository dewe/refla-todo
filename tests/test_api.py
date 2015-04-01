from copy import copy
from flask import json
from refla import db, app as refla

tasks = [
    {'id':1, 'title': u'test1', 'done': False},
    {'id':2, 'title': u'test2', 'done': True}
]

class TestApi:
    
    def setup(self):
        refla.app.config['TESTING'] = True
        self.app = refla.app.test_client()

    def setup_method(self, method):
        db.data = copy(tasks)

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
        assert response.data == json.dumps({ 'message': '404: Not Found' }, indent=2)

    def test_get_task_bad_id(self):
        response = self.app.get('/api/tasks/foul_id')
        assert response.status_code == 404

    def test_post_new_task(self):
        response = self.app.post('/api/tasks', 
                                 data='{"title":"foo"}', 
                                 content_type='application/json')
        assert response.status_code == 201
        assert json.loads(response.data)['task']['id'] == 3
        assert len(db.data) == 3

    def test_post_new_task_non_json(self):
        response = self.app.post('/api/tasks', 
                                 data='{"title":"foo"}')
        assert response.status_code == 400

    def test_post_new_task_no_title(self):
        response = self.app.post('/api/tasks', 
                                 data='{}', 
                                 content_type='application/json')
        assert response.status_code == 400

    def test_put_update_task(self):
        response = self.app.put('/api/tasks/1', 
                                data='{"title":"updated", "done": true}', 
                                content_type='application/json')
        assert response.status_code == 200
        assert json.loads(response.data)['task'] == {'id':1, 'title':'updated', 'done':True}
        response = self.app.get('/api/tasks/1')
        assert json.loads(response.data)['task'] == {'id':1, 'title':'updated', 'done':True}

    def test_put_update_task_not_found(self):
        response = self.app.put('/api/tasks/3',
                                data='{"title":"updated", "done": true}', 
                                content_type='application/json')
        assert response.status_code == 404

    def test_put_update_task_validate_title(self):
        response = self.app.put('/api/tasks/1',
                                data='{"title":1234556}', 
                                content_type='application/json')
        assert response.status_code == 400

    def test_put_update_task_validate_done(self):
        response = self.app.put('/api/tasks/1', 
                                data='{"done":1234556}', 
                                content_type='application/json')
        assert response.status_code == 400


