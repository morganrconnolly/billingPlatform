# Flask React Boilerplate

Production-ready, one-click deployable boilerplate for [React](http://facebook.github.io/react/), [Webpack](http://webpack.github.io/), [Flask](http://flask.pocoo.org/) and [PostgreSQL](http://www.postgresql.org/).

## One-click production deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alexkuz/flask-react-boilerplate)

This is what you will get:

https://flask-react-boilerplate.herokuapp.com/

## Local installation

You'll neel a little more than one click.

**Prerequisites**:

- Pip (https://pip.pypa.io/en/latest/installing.html)
- PostgreSQL (http://www.postgresql.org/download/)
- NPM (https://docs.npmjs.com/getting-started/installing-node)

Clone repository:

```
git clone https://github.com/alexkuz/flask-react-boilerplate.git

cd react-webpack-boilerplate
```

Install npm dependencies:

```
npm install
```

Setup python environment and install dependencies:

```
virtualenv venv

source venv/bin/activate     # or venv/bin/activate.fish or whatever

pip install -r requirements.txt
```

Copy `.env.example` config file to `.env`:

```
cp .env.example .env
```

Start PostgreSQL service if needed:

```
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
```

Create database tables:

```
heroku local initdb
```

Finally, start local server:

```
heroku local web

open http://localhost:3001
```

## What do we have here?

- A basket of kittens 🐱
- Simple Flask **API**, powered with [**Flask-RESTful**](https://flask-restful.readthedocs.org/en/0.3.3/), [**SQLAlchemy**](http://www.sqlalchemy.org/) and [**PostgreSQL**](http://www.postgresql.org/)
- **UI**, powered with [**React**](http://facebook.github.io/react/), [**Babel**](https://babeljs.io/), [**Webpack**](http://webpack.github.io/) and [**React Transform HMR**](https://github.com/gaearon/react-transform-hmr)

## License

Copyright 2015, Alexander Kuznetsov &lt;alexkuz@gmail.com&gt;

This boilerplate is based on [**React Webpack Boilerplate**](https://github.com/srn/react-webpack-boilerplate): MIT © [Søren Brokær](http://srn.io)
