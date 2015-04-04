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
    var task = {title: taskText}
    var newTasks = this.state.tasks.concat([task]);
    this.setState({tasks: newTasks});
    console.log('todo: call api update with task', task);
  },

  updateTask: function(task) {
    this.setState({tasks: this.state.tasks});
    console.log('todo: call api update with task', task);
  },

  render: function() {
    var remaining = this.state.tasks.filter(function(t){return !t.done}).length;
    return (
      <div>
        <TodoInput handleNewTask={this.addTask} />
        <TodoList items={this.state.tasks} handleItemUpdate={this.updateTask} />
        <div>{remaining} items left</div>
      </div>
    );
  }
});
