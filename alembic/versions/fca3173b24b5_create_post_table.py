"""create post table

Revision ID: fca3173b24b5
Revises: 
Create Date: 2026-08-26 11:52:48.004780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fca3173b24b5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('post', 
                    sa.Column('id', sa.Integer(), nullable = False, primary_key=True),
                    sa.Column("title", sa.String(), nullable = False)
)
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('posts')
    """Downgrade schema."""
    pass
