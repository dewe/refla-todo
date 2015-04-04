var React = require('react');
var TodoInput = require('./TodoInput.react');
var TodoList = require('./TodoList.react');
var tasksvc = require('../tasksvc')

module.exports = TodoApp = React.createClass({
  getInitialState: function() {
    return {tasks: []};
  },

  componentDidMount: function() {
    var self = this;
    tasksvc.getTasks(function(err, tasks) {
        self.setState({tasks: tasks});
    });
  },

  addTask: function(taskText) {
    var newTasks = this.state.tasks.concat([taskText]);
    this.setState({tasks: newTasks});
  },

  onToggle: function(x) {
    console.log('onToggle', x);
  },

  render: function() {
    var remaining = this.state.tasks.filter(function(t){return !t.done}).length;
    return (
      <div>
        <TodoInput handleNewTask={this.addTask} />
        <TodoList items={this.state.tasks} onToggle={this.onToggle} />
        <div>{remaining} items left</div>
      </div>
    );
  }
});
