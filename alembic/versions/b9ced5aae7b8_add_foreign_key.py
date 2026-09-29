"""add foreign key

Revision ID: b9ced5aae7b8
Revises: da8ad3a54ca6
Create Date: 2026-08-26 17:23:36.294908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9ced5aae7b8'
down_revision: Union[str, Sequence[str], None] = 'da8ad3a54ca6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="post", referent_table="user",
        local_cols=['user_id'], 
        remote_cols=['id'], 
        ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name="post")
    op.drop_column('post', 'user_id')
    pass
