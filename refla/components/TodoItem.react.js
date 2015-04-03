var React = require('react');

module.exports = TodoItem = React.createClass({
  render: function() {
    return (
      <li>
        <input type='checkbox' onChange={this.props.onToggle} defaultChecked={this.props.item.done} />
        <label>{this.props.item.title}</label> 
      </li>
    );
  }
});