var React = require('react');
var TodoInput = require('./TodoInput.react')
var TodoList = require('./TodoList.react');

module.exports = TodoApp = React.createClass({
  getInitialState: function() {
    return {tasks: []};
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
