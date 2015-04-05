var React = require('react');

module.exports = React.createClass({
  getInitialState: function () {
    return {text: ''};
  },

  onChange: function(e) {
    this.setState({text: e.target.value});
  },

  handleSubmit: function(e) {
    e.preventDefault(); // prevent browser submitting form
    this.props.handleNewTask(this.state.text);
    this.setState({text: ''});
  },

  render: function() {
    return (
      <form onSubmit={this.handleSubmit} className='todo-input'>
        <input
          onChange={this.onChange}
          value={this.state.text}
          placeholder='What needs to be done?' />
        <button>Add Todo</button>
      </form>
    );
  }
});