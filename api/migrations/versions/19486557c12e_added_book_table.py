"""added book table

Revision ID: 19486557c12e
Revises: 
Create Date: 2021-06-17 12:30:40.141132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19486557c12e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('primary_isbn10', sa.String(length=32), nullable=True, index=True),
    sa.Column('primary_isbn13', sa.String(length=32), nullable=True, index=True),
    sa.Column('publisher', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_book'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
