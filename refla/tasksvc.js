var request = require('browser-request');

exports.getTasks = function(callback) {
  var uri = '/api/tasks';
  logApiCall(uri);
  request({method:'GET', uri:uri, json:true}, function(error, response, body) {
    if (error) {
      console.error(error);
    };
    callback(error, body.tasks);
  });
}; 

exports.updateTask = function(task, callback) {
  var uri = task.uri;
  logApiCall(uri, task);
  request({method:'PUT', uri:uri, json:task}, function(error, response, body) {
    if (error) {
      console.error(error);
    };
    callback && callback(error, body.task);
  });
}; 

function logApiCall(uri, payload) {
  console.log('calling api: %s', uri, payload);
}
