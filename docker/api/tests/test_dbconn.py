import os
import pytest

from sqlalchemy import create_engine

from app.models import db, Word


@pytest.fixture
def mockword_value():
    return "Testing!"


def test_connection_url():
    db_url = os.environ['DATABASE_URL']
    eng = create_engine(db_url)
    assert type(eng.table_names()) == list
    assert 'production' in db_url


def test_connection_with_test_app(app):
    db_url = app.config['DATABASE_URL']
    assert 'production' not in db_url
    assert app.config['DATABASE_URL'] == app.config['SQLALCHEMY_DATABASE_URI']


def test_connection_with_db(db):
    assert type(db.engine.table_names()) == list


def test_transactions_are_isolated_first_txn(db, mockword_value):
    word = Word(value=mockword_value, score=10)
    db.session.add(word)
    db.session.commit()
    assert Word.query.get(mockword_value) is not None


def test_transactions_are_isolated_second_txn(db, mockword_value):
    assert Word.query.get(mockword_value) is None
