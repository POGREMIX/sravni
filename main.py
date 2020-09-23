from flask import Flask
from flask import render_template, url_for
from flask_bootstrap import Bootstrap
from routes.text_route import text_route
from routes.index_route import index_route

application = Flask(__name__)

bootstrap = Bootstrap(application)

application.register_blueprint(text_route)
application.register_blueprint(index_route)


if __name__ == '__main__':
    application.debug = True
    # print(application.url_map)
    application.run()
