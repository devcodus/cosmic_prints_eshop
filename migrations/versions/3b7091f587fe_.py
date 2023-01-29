"""empty message

Revision ID: 3b7091f587fe
Revises: 2ad856c7c78b
Create Date: 2023-01-28 19:52:38.862043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b7091f587fe'
down_revision = '2ad856c7c78b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('product_price_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_unique_constraint('product_price_key', ['price'])

    # ### end Alembic commands ###