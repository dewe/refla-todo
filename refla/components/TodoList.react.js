var React = require('react');

module.exports = TodoList = React.createClass({
  render: function() {
    return <ul>{this.props.items.map(createItem)}</ul>;
  }
});

function createItem(task) {
  return (
    <li>
      <input type='checkbox' />
      <label>{task.title}</label>
    </li>
  );
};

