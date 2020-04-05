from flask import render_template, redirect, url_for
from flask import session

from {{cookiecutter.project_slug}}.main import bp

"""This route is requested, whenever (and only if) the user changed the language manually"""
@bp.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('main.index'))


@bp.route('/')
def root():
    return redirect((url_for('main.index')))


@bp.route('/index')
def index():
    return render_template('index.html')