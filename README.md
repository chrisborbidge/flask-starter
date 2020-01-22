# flask-starter

[![Build Status](https://travis-ci.com/chrisborbidge/flask-starter.svg?branch=master)](https://travis-ci.com/chrisborbidge/flask-starter)

Very basic flask starter, with Bootstrap.

### Quick start

#### Development
```
python -m venv .venv
pip install -r "requirements.txt"
python3 application.py
```

#### Production
```
pip install -r "requirements.txt"
gunicorn application:app
```
