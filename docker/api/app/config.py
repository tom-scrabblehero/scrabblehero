import os


class ProductionConfig(object):
    TESTING = False
    DEBUG = False

    DATABASE_URL = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(ProductionConfig):
    TESTING = True

    DATABASE_URL = os.environ['DATABASE_URL'].replace("production", "testing")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class DevelopmentConfig(ProductionConfig):
    DEBUG = True
