from flask import Blueprint, redirect, url_for, flash
from flask import render_template

error_route = Blueprint('error_route', __name__)


@error_route.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error_mess=error), 500
