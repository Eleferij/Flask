"""user tokens

Revision ID: 965881e4717f
Revises: 73eadae1b8df
Create Date: 2021-05-30 15:40:58.257897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '965881e4717f'
down_revision = '73eadae1b8df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_column('users', 'token_expiration')
    op.drop_column('users', 'token')
    # ### end Alembic commands ###