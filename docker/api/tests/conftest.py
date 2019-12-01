import os
import pytest
import sqlalchemy

from app import create_app
from app.models import db as _db



@pytest.fixture(scope='session')
def dbconn():
    engine = sqlalchemy.engine.create_engine(os.environ['DATABASE_URL'])
    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT").execute('drop database if exists testing;')
    conn.execution_options(isolation_level="AUTOCOMMIT").execute('create database testing;')
    return dbconn


@pytest.fixture(scope="session")
def app(dbconn):
    return create_app(environment="testing")


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def database(app, client):
    with app.app_context():
        _db.drop_all()
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture()
def db(database):
    database.session.rollback()
    database.session.begin(subtransactions=True)
    yield database
    database.session.rollback()
