import os

from {{cookiecutter.app_name}} import create_app


{{cookiecutter.app_name}} = create_app(os.getenv('FLASK_CONFIG') or 'default')