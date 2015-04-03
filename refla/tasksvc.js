
exports.getTasks = function(callback) {
    var request = new XMLHttpRequest(), self = this;

    request.open('GET', '/api/tasks', true);

    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var body = JSON.parse(request.responseText); //todo: try/catch
        var newTasks = body.tasks.map(function(t){return t.title});
        callback(null, newTasks);
      } else {
        callback(request.status);
      }
    };

    request.send();

}