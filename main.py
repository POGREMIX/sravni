from flask import Flask
from flask import render_template, url_for
from flask_bootstrap import Bootstrap

from routes.error_route import error_route
from routes.text_route import text_route
from routes.index_route import index_route
from routes.user_route import user_route


application = Flask(__name__)

bootstrap = Bootstrap(application)

application.register_blueprint(text_route)
application.register_blueprint(index_route)
application.register_blueprint(user_route)
application.register_blueprint(error_route)


if __name__ == '__main__':
    # application.debug = True
    application.config['SECRET_KEY'] = 'a really really really really long secret key'
    # print(application.url_map)
    application.run()
