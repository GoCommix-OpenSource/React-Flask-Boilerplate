from flask import render_template
from core import create_app, BASE_DIR

if __name__ == '__main__':
    app=create_app(__name__)
    @app.route('/', methods=['GET'], defaults={'path': ''})
    @app.route("/<path:path>")
    def home(path):
        return render_template("index.html")
    
    app.run()