"""added messages table

Revision ID: be9fa729c375
Revises: bf8c368942b7
Create Date: 2020-12-15 13:58:41.934661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be9fa729c375'
down_revision = 'bf8c368942b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('messages', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.postid'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.profileid'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
