import os

from core.factories import BASE_DIR

class Config:
    '''Common config setting goes in this class'''
    SECRET_KEY = os.urandom(32)
    STATIC_FOLDER = BASE_DIR/'app/views'
    TEMPLATE_FOLDER = BASE_DIR/'app/views'
    
class DevConfig(Config):
    '''Development config setting goes in this class'''
    DEBUG = True
    DEVELOPMENT = True
    MONGO_SETTINGS = {
        'host':'mongodb://localost:27017/testDB',
        'connect':True
    }

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    
class ProdConfig(Config):
    '''Production config setting goes in this class'''
    DEBUG = False
    TESTING = False