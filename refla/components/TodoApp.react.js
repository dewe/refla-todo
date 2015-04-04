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
    var task = {title: taskText}, self = this;
    tasksvc.addTask(task, function(err, newTask) {
      var newTasks = self.state.tasks.concat([newTask]);
      self.setState({tasks: newTasks});    
    });
  },

  updateTask: function(task) {
    this.setState({tasks: this.state.tasks});
    tasksvc.updateTask(task);
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
