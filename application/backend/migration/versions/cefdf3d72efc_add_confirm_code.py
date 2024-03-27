"""'add_confirm_code'

Revision ID: cefdf3d72efc
Revises: 7453ace70af8
Create Date: 2024-03-19 12:27:47.091673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cefdf3d72efc'
down_revision: Union[str, None] = '7453ace70af8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirm_code', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirm_code')
    # ### end Alembic commands ###
