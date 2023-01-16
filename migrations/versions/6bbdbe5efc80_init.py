"""init

Revision ID: 6bbdbe5efc80
Revises: 
Create Date: 2023-01-13 01:04:05.482811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bbdbe5efc80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('flask_users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_flask_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flask_users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_flask_users_username'))

    op.drop_table('flask_users')
    # ### end Alembic commands ###
