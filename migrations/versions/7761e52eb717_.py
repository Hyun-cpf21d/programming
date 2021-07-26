"""empty message

Revision ID: 7761e52eb717
Revises: af17dc9ab78e
Create Date: 2021-07-24 13:41:51.836603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7761e52eb717'
down_revision = 'af17dc9ab78e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video_info', sa.Column('video_duration', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video_info', 'video_duration')
    # ### end Alembic commands ###