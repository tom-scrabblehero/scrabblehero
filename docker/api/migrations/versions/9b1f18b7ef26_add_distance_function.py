"""Add distance function

Revision ID: 9b1f18b7ef26
Revises: b692c9c63691
Create Date: 2019-12-03 17:14:55.291723

"""
import os

from alembic import op
import sqlalchemy as sa

from app.utils import data_dir


# revision identifiers, used by Alembic.
revision = '9b1f18b7ef26'
down_revision = 'b692c9c63691'
branch_labels = None
depends_on = None


def upgrade():
    func_text = open(os.path.join(data_dir, 'pgfunctions', 'distance.sql')).read()
    op.execute(func_text)


def downgrade():
    op.execute('drop function if exists distance')
