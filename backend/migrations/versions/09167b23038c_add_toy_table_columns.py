"""add toy table columns

Revision ID: 09167b23038c
Revises: 
Create Date: 2024-01-11 12:13:22.813977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09167b23038c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('toy_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toy_table')
    # ### end Alembic commands ###