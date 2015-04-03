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
* URIs instead of IDs: not exactly hateoas, but improves dev experience.


## Possible future improvements

* Test coverage of client side code
* Enable compression of static files
* Enable http caching of bundle.js, including a cache buster
* Use flask blueprints to factor app into separate web and api components.
* An actual database.
* Api auth, multiple concurrent users.
