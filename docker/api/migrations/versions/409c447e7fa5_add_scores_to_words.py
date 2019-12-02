"""add scores to words

Revision ID: 409c447e7fa5
Revises: 2a7dc6e07fdc
Create Date: 2019-12-02 20:57:36.509661

"""

import os

from alembic import op
import sqlalchemy as sa

from app.utils import data_dir



# revision identifiers, used by Alembic.
revision = '409c447e7fa5'
down_revision = '2a7dc6e07fdc'
branch_labels = None
depends_on = None


def upgrade():
    func_text = open(os.path.join(data_dir, 'pgfunctions', 'score.sql')).read()
    op.execute('create extension if not exists plv8')
    op.execute(func_text)


def downgrade():
    op.execute('drop function score')
    op.execute('drop extension plv8')
