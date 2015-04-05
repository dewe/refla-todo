var React = require('react');
var TodoItem = require('./TodoItem.react');

module.exports = TodoList = React.createClass({
  createItem: function(item) {
    return <TodoItem key={item.uri} item={item} handleItemUpdate={this.props.handleItemUpdate} />
  },

  render: function() {
    return <ul className='todo-list'>{this.props.items.map(this.createItem)}</ul>;
  }
});


