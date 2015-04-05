var React = require('react');
var TodoInput = require('./TodoInput.react');
var TodoList = require('./TodoList.react');
var tasksvc = require('../tasksvc');

module.exports = React.createClass({
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
    tasksvc.updateTask(task);
    this.setState({tasks: this.state.tasks});
  },

  markAllDone: function() {
    var notDone = this.remainingTasks();
    for (var i = 0; i < notDone.length; i++) {
      var task = notDone[i];
      task.done = true;
      this.updateTask(task);
    }
  },

  remainingTasks: function() {
    return this.state.tasks.filter(function(task) { return !task.done; });
  },

  render: function() {
    var count = this.remainingTasks().length;
    return (
      <div id="todo-container">
        <h1 className='header'>Todos</h1>
        <TodoInput handleNewTask={this.addTask} />
        <TodoList items={this.state.tasks} handleItemUpdate={this.updateTask} />
        <div className='footer'>
          <div className='items-left'>{count} items left</div>
          <div onClick={this.markAllDone} className='mark-complete'>Mark all as complete</div>
        </div>
      </div>
    );
  }
});
