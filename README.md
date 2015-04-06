# refla-todo

Description TBD

API is live at [http://refla.herokuapp.com/api](http://refla.herokuapp.com/api)


## Installation in local setup

```bash
$ virtualenv env
$ pip install -r requirements.txt
$ setup.py install
```

## Design choices

__Backend:__
* Flask: just because. And for its lightness, its testability and the fun of it.
* Pytest: if you should have only one testing framework for python, go with pytest.
* Gunicorn: WSGI + heroku = true.

__Frontend:__
* React: slim, isomorphic (if server == node), well designed and to the point. Do one thing and do it well. Seems right to me.
* Browserify: running node style commonjs modules on the browser is sweet, and essential, to a backend dev.

__Rest API:__
* No trailing slashes: avoid HTTP redirects by mistake.
* URIs instead of IDs: not exactly hateoas, but improves usage/dev experience.


## Todos and possible future improvements

__Dev:__
* Test coverage of client side code
* Apply jslinting/hinting
* Move components and tasksvc into node_modules/app for cleaner references.
* Use gulp or grunt instead of npm script element.

__App:__
* Mobile CSS
* Enable compression of static files
* Enable http caching of bundle.js, including a cache buster
* Use flask blueprints to factor app into separate web and api components.
* An actual database.
* Api auth.

__Features:__
* This feature list as app initial data.
* Reorder tasks - drag and drop.
* Multiple lists
* Private lists
* Shared lists, concurrent use, socket.io.
* Inline edit of tasks.
* Task descriptions, i.e. more than just a title.
* Better API error messages for status 400.
* Handle retries of api calls, in case of failures.
