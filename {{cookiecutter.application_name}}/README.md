# {{ cookiecutter.application_name }}

## Getting start

```bash
set FLASK_APP={{ cookiecutter.application_name }}:{{cookiecutter.app_name}}

flask run
```

or

```bash
flask --app {{ cookiecutter.application_name }}:{{cookiecutter.app_name}} run
```
