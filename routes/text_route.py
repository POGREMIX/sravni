from flask import Blueprint
from flask import render_template


text_route = Blueprint('text_route', __name__)


@text_route.route('/text/<int:text_id>/')
def text(text_id):
    return render_template('text.html', text_id=text_id)