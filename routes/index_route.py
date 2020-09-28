from flask import render_template, Blueprint, request, get_flashed_messages

index_route = Blueprint('index_route', __name__)


@index_route.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    print(messages)

    return render_template('index.html', ip=request.remote_addr, agent=request.user_agent)
