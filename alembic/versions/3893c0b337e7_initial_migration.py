"""Initial migration

Revision ID: 3893c0b337e7
Revises: 6ff27be083f4
Create Date: 2025-05-13 00:21:45.937315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3893c0b337e7'
down_revision: Union[str, None] = '6ff27be083f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
