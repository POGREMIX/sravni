from flask import render_template, Blueprint, request


index_route = Blueprint('index_route', __name__)


@index_route.route('/')
def hello_world():
    return render_template('index.html', ip=request.remote_addr, agent=request.user_agent)
