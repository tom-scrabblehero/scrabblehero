"""Add related word

Revision ID: b692c9c63691
Revises: a92d027328dd
Create Date: 2019-12-03 16:25:40.512291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b692c9c63691'
down_revision = 'a92d027328dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('related_word',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('related', sa.String(), nullable=False),
    sa.Column('score_difference', sa.Integer(), nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.Column('recommendation', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['word'], ['word.value'], ),
    sa.PrimaryKeyConstraint('word', 'related')
    )
    op.create_index(op.f('ix_related_word_distance'), 'related_word', ['distance'], unique=False)
    op.create_index(op.f('ix_related_word_score_difference'), 'related_word', ['score_difference'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_related_word_score_difference'), table_name='related_word')
    op.drop_index(op.f('ix_related_word_distance'), table_name='related_word')
    op.drop_table('related_word')
    # ### end Alembic commands ###