var React = require('react');

module.exports = TodoItem = React.createClass({
  onChange: function() {
    var task = this.props.item;
    task.done = !task.done;
    this.props.handleItemUpdate(task);
  },

  render: function() {
    return (
      <li className='todo-item'>
        <input type='checkbox' onChange={this.onChange} checked={this.props.item.done} />
        <span>{this.props.item.title}</span> 
      </li>
    );
  }
});