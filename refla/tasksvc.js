var request = require('browser-request');

exports.getTasks = function(callback) {
  var options = {method:'GET', uri:'/api/tasks'};
  apiJsonRequest(options, function(err, res, json) {
    callback && callback(err, json.tasks);
  });
}; 

exports.addTask = function(task, callback) {
  var options = {method:'POST', uri: '/api/tasks', json:task};
  apiJsonRequest(options, function(err, res, json) {
    callback && callback(err, json.task);
  });
}; 

exports.updateTask = function(task, callback) {
  var options = {method:'PUT', uri:task.uri, json:task}
  apiJsonRequest(options, function(err, res, json) {
    callback && callback(err, json.task);
  });
}; 

function apiJsonRequest(options, callback) {
  options.json = options.json || true;
  console.log('api call', options);
  request(options, logError(callback));
}

function logError(callback) {
  return function(err, response, body) {
    if (err) {
      console.error(err);
    }
    callback(err, response, body);
  }
}
