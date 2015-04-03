var React = require('react');
var TodoInput = require('./TodoInput.react');
var TodoList = require('./TodoList.react');

module.exports = TodoApp = React.createClass({
  getInitialState: function() {
    return {tasks: []};
  },

  componentDidMount: function() {
    var request = new XMLHttpRequest(), self = this;
    request.open('GET', '/api/tasks', true);
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var body = JSON.parse(request.responseText); //todo: try/catch
        var newTasks = body.tasks.map(function(t){return t.title});
        self.setState({tasks: newTasks});
      }
    };

    request.send();
  },

  addTask: function(taskText) {
    var newTasks = this.state.tasks.concat([taskText]);
    this.setState({tasks: newTasks});
  },

  render: function() {
    return (
      <div>
        <TodoInput handleNewTask={this.addTask} />
        <TodoList tasks={this.state.tasks} />
      </div>
    );
  }
});
