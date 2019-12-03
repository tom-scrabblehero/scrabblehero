import os
import datetime as dt
import psycopg2
from psycopg2.extras import execute_values
import sqlalchemy as sa

from flask import current_app
from flask.cli import AppGroup, click

from .utils import WordGenerator, data_dir
from .models import db, Word

seed = AppGroup('seed', help="Commands to seed the database")


@seed.command()
@click.option('--drop', default=False, is_flag=True, help="Drop any existing words")
def words(drop):
    current_app.logger.info("Seeding words")
    url = sa.engine.url.make_url(current_app.config['DATABASE_URL'])
    conn = psycopg2.connect(user=url.username, password=url.password, host=url.host, dbname=url.database)
    cursor = conn.cursor()

    if drop:
        current_app.logger.info("Dropping existing words")
        cursor.execute("delete from word where 1=1;")
    else:
        current_app.logger.info("Retaining existing words")

    query = "insert into word (created_at, updated_at, value, score) values %s"
    words = WordGenerator().generate_words(as_tuples=True)
    current_app.logger.info("Starting insert")
    execute_values(cursor, query, words, page_size=10000)
    conn.commit()
    total_words = Word.query.count()
    current_app.logger.info(f"Finished insert. Total inserted words: {total_words}")


@seed.command()
@click.option('--drop', default=False, is_flag=True, help="Drop any existing words")
def recommendations(drop):
    current_app.logger.warning("Seeding recommendations")


    if drop:
        current_app.logger.warn("Dropping existing words")
        db.engine.execute("delete from related_word where 1=1;")
    else:
        current_app.logger.warn("Retaining existing recommendations")

    character_pairs = WordGenerator().generate_character_pairs()
    sql_template = open(os.path.join(data_dir, 'models', 'word_recommendations.sql')).read()
    for n, (lower_bound, upper_bound) in enumerate(character_pairs):
        current_app.logger.warning(f"Seeding #{n+1} out of {len(character_pairs)} reccommendations: lowerbound={lower_bound} upperbound={upper_bound}")
        sql = sql_template.format(lower_bound=lower_bound, upper_bound=upper_bound)
        start = dt.datetime.now()
        db.session.execute(sql)
        db.session.commit()
        end = dt.datetime.now()
        current_app.logger.warning(f"Finished in {end - start} seconds")
