"""add user table

Revision ID: da8ad3a54ca6
Revises: e024f6ab3c3d
Create Date: 2026-08-26 17:15:18.660967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da8ad3a54ca6'
down_revision: Union[str, Sequence[str], None] = 'e024f6ab3c3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('user')
    """Downgrade schema."""
    pass
