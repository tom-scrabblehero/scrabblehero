"""Change hash id type

Revision ID: ea246209833b
Revises: 9f35579719c1
Create Date: 2019-12-11 16:58:41.847078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea246209833b'
down_revision = '9f35579719c1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("alter table word alter column anagram_hash set data type varchar")


def downgrade():
    op.execute("alter table word alter column anagram_hash set data type bigint using anagram_hash::bigint")
