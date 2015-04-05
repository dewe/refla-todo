'use strict';
var React = require('react');
var TodoApp = require('./components/TodoApp.react');

React.render(
    React.createElement(TodoApp), 
    document.getElementById('react-mount')
);