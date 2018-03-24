# TaskManager

Task manager is very simple application. It is only for testing purpose case.

## Deployment - without source
```bash
  virtualenv ./venv
  source ./venv/bin/activate
  pip install git+https://github.com/euroska/uplus
  taskmanager migrate
  taskmanager initdb
  taskmanager runserver
```
Inicialize empty application with user admin:admin is superuser role and user test:test in staf role.

## Deployment with sources
```bash
  git clone https://github.com/euroska/uplus
  cd uplus
  virtualenv ./venv
  source ./venv/bin/activate
  pip install -U --editable ./
  taskmanager migrate
  taskmanager loaddata fixtures.json
  taskmanager runserver
```

taskmanager is alias for ```./manage.py``` file from django, so you can use attributes like ```--settings```.
For list of command you can use taskmanager help

You can load default data by:

```bash
taskmanager loaddata fixures.json
```

## Run
```bash
taskmanager runserver # start application localy: http://localhost:8000/
```

There are many ways, how to deploy.
There is wsgi application wrapper ```taskmanager.wsgi.application```.

Default user (privileged) is admin:admin and (simple) test:test
