import datetime as dt

from flask import current_app
from flask.cli import AppGroup

from .utils import WordGenerator
from .models import db, Word

seed = AppGroup('seed', help="Commands to seed the database")


# This is very slow on production because it seems impossible to get SQLAlchemy
# to issue multiple INSERT commands in a single query. I think we need an
# alternative method for bulk inserting objects. One idea is to use pgcopy
# and send a csv
@seed.command()
def words():
    """
    Add the wordnet words to the database
    """

    current_app.logger.info("Seeding words")
    words = WordGenerator().generate_words()
    current_app.logger.info(f"Generated {len(words)} words to insert")
    created_at = updated_at = dt.datetime.now()
    for word in words:
        word.update({'created_at': created_at, 'updated_at': updated_at})
    else:
        current_app.logger.info("Updated timestamps on words")

    db.session.bulk_insert_mappings(Word, words)
    db.session.commit()

    current_app.logger.info("Finished inserting words")