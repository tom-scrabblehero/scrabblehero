import os

from sqlalchemy import create_engine


def test_connection_url():
    db_url = os.environ['DATABASE_URL']
    eng = create_engine(db_url)
    assert type(eng.table_names()) == list
    assert 'production' in db_url


def test_connection_with_test_app(app):
    db_url = app.config['DATABASE_URL']
    assert 'production' not in db_url
