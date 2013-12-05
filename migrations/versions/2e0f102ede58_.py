"""empty message

Revision ID: 2e0f102ede58
Revises: 20024877d55c
Create Date: 2013-12-03 12:24:21.067840

"""

# revision identifiers, used by Alembic.
revision = '2e0f102ede58'
down_revision = '20024877d55c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('email', 'person')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('email', 'person', [u'email'], unique=True)
    op.drop_table('articles')
    ### end Alembic commands ###
