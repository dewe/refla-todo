var React = require('react');

module.exports = TodoList = React.createClass({
  render: function() {
    return <ul>{this.props.tasks.map(createItem)}</ul>;
  }
});

function createItem(text) {
  return <li>{text}</li>;
};

