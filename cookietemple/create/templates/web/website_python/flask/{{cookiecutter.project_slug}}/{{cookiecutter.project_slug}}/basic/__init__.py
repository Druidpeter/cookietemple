from flask import Blueprint

bp = Blueprint('basic', __name__)

from {{cookiecutter.project_slug}}.basic import routes  # noqa: E402, F401
