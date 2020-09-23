from flask import Flask
from flask import render_template, url_for
from flask_bootstrap import Bootstrap
from routes.text_route import text_route
from routes.index_route import index_route

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.register_blueprint(text_route)
app.register_blueprint(index_route)


if __name__ == '__main__':
    app.debug = True
    print(app.url_map)
    app.run()
