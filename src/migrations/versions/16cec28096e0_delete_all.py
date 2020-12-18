"""delete all

Revision ID: 16cec28096e0
Revises: be9fa729c375
Create Date: 2020-12-18 13:11:38.127053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16cec28096e0'
down_revision = 'be9fa729c375'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('messages', 'profile_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'profile_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('messages', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###