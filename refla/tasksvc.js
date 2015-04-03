
exports.getTasks = function(callback) {
    var request = new XMLHttpRequest();

    request.open('GET', '/api/tasks', true);

    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var body = JSON.parse(request.responseText); //TODO: try/catch
        callback(null, body.tasks);
      } else {
        callback(request.status);
      }
    };

    request.send();
}