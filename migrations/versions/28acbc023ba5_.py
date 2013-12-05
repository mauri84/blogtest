"""empty message

Revision ID: 28acbc023ba5
Revises: ec6eabee2e1
Create Date: 2013-12-04 12:40:24.286330

"""

# revision identifiers, used by Alembic.
revision = '28acbc023ba5'
down_revision = 'ec6eabee2e1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('person_name', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'person_name')
    ### end Alembic commands ###
