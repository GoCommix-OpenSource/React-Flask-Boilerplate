from flask_mongoengine import MongoEngine

# initialise extentions
db = MongoEngine()


# registers extentions
def register_extensions(app):
    db.init_app(app)
    return None
