import os


class ProductionConfig(object):
    TESTING = False
    DEBUG = False

    DATABASE_URL = os.environ['DATABASE_URL']


class TestingConfig(ProductionConfig):
    TESTING = True

    DATABASE_URL = os.environ['DATABASE_URL'].replace("production", "testing")


class DevelopmentConfig(ProductionConfig):
    DEBUG = True
