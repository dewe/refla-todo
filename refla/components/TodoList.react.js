var React = require('react');
var TodoItem = require('./TodoItem.react');

module.exports = TodoList = React.createClass({
  render: function() {
    return <ul>{this.props.items.map(this.createItem)}</ul>;
  },

  createItem: function (item) {
    return <TodoItem item={item} onToggle={this.props.onToggle} />
  }
});


