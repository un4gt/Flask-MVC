# Flask-MVC

[Cookiecutter](https://github.com/cookiecutter/cookiecutter.git) template to create new [flask](https://github.com/pallets/flask) application to build a Web API.

## Layout

Project Layout from [miguelgrinberg/flasky: Companion code to my O'Reilly book "Flask Web Development", second edition.](https://github.com/miguelgrinberg/flasky)

```text
│  .gitignore
│  cookiecutter.json
│  LICENSE
│  README.md
│
└─{{cookiecutter.application_name}}
    │  .gitignore
    │  config.py
    │  README.md
    │  {{cookiecutter.application_name}}.py
    │
    ├─tests
    │      __init__.py
    │
    └─{{cookiecutter.app_name}}
        │  exceptions.py  # your custom exceptions
        │  __init__.py    # create_app function here
        │
        ├─main            # your main blueprint
        │      errors.py  # web errors like 404, 403
        │      views.py   # just have index route
        │      __init__.py
        │
        ├─models          # database models here
        │      __init__.py
        │
        ├─static          # static file folder
        │      .gitkeep
        │
        └─templates
                403.html  # forbidden page
                404.html  # not found page
                500.html  # internal server error page
                base.html # base template to extends
                index.html # home page
```

## How to use

### With [Cookiecutter](https://github.com/cookiecutter/cookiecutter.git)

#### Install Cookiecutter

```bash
pip install --upgrade cookiecutter
```

#### Create a new project

#### With `cookiecutter`

```bash
cookiecutter https://github.com/un4gt/Flask-MVC
```

#### With [Flasky-Cli](https://github.com/un4gt/flasky-cli)

##### Install Flasky-Cli

```bash
pip install --upgrade flasky-cli
```

##### Create new project

```bash
flasky-cli create
```

and choice `Flask-API` template.

## Initialize project and run

You can use tools like pdm, pipenv, poetry or rye to init and run your project.
