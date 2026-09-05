"""Add token limits to users

Revision ID: add_token_limits
Revises: 
Create Date: 2024-12-20

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'add_token_limits'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Добавляем колонки для лимитов токенов
    op.add_column('users', sa.Column('tokens_limit', sa.Integer(), nullable=False, server_default='400000'))
    op.add_column('users', sa.Column('tokens_used', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('users', sa.Column('tokens_reset_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('tokens_frozen', sa.Boolean(), nullable=False, server_default='0'))


def downgrade():
    # Удаляем колонки при откате миграции
    op.drop_column('users', 'tokens_frozen')
    op.drop_column('users', 'tokens_reset_date')
    op.drop_column('users', 'tokens_used')
    op.drop_column('users', 'tokens_limit')
