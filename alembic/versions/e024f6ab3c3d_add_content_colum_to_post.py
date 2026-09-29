"""add content colum to post

Revision ID: e024f6ab3c3d
Revises: fca3173b24b5
Create Date: 2026-08-26 14:52:43.019958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e024f6ab3c3d'
down_revision: Union[str, Sequence[str], None] = 'fca3173b24b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('post', sa.Column('content', sa.String(), nullable = False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('post', 'content')
    """Downgrade schema."""
    pass
