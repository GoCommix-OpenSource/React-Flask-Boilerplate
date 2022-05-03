from flask import Flask
from .extentions import *
from .config import *
from .factories import *




def create_app(app_name):
    flask_app = Flask(
        app_name,
        # static_folder=BASE_DIR/"app/views/static/",
        template_folder=BASE_DIR/"app/views/",
        static_url_path="/static",
    )
    print(f'''
    Flask app Initialized: {app_name}
    STATIC folder: {flask_app.static_folder}      
    TEMPLATE folder: {flask_app.template_folder}      
    ''')
    flask_app.config.from_object(setting_name)
    flask_app.app_context().push()

    # register_logger(flask_app)
    register_extensions(flask_app)
    # register_api(cnnx_app)

    return flask_app
