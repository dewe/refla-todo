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
        data = json.loads(response.data)
        assert response.status_code == 200
        assert len(data['tasks']) == 2

    def test_get_task(self):
        response = self.app.get('/api/tasks/2')
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['task'] == {'uri':'http://localhost/api/tasks/2', 'title':'test2', 'done':True}

    def test_get_task_not_found(self):
        response = self.app.get('/api/tasks/4711')
        data = json.loads(response.data)
        assert response.status_code == 404
        assert data == { 'message': '404: Not Found' }

    def test_get_task_bad_id(self):
        response = self.app.get('/api/tasks/foul_id')
        assert response.status_code == 404

    def test_post_new_task(self):
        response = self.app.post('/api/tasks', 
                                 data='{"title":"foo"}', 
                                 content_type='application/json')
        data = json.loads(response.data)
        assert response.status_code == 201
        assert data['task']['uri'] == 'http://localhost/api/tasks/3'
        tasks = json.loads(self.app.get('/api/tasks').data)['tasks']
        assert len(tasks) == 3

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
        data = json.loads(response.data)
        assert response.status_code == 200
        task = json.loads(self.app.get('/api/tasks/1').data)['task']
        assert task == {'uri':'http://localhost/api/tasks/1', 'title':'updated', 'done':True}

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

    def test_delete_task(self):
        response = self.app.delete('/api/tasks/2')
        assert response.status_code == 200
        tasks = json.loads(self.app.get('/api/tasks').data)['tasks']
        assert len(tasks) == 1


