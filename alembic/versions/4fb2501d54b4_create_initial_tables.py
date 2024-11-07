"""create initial tables

Revision ID: 4fb2501d54b4
Revises: 592bead63eb0
Create Date: 2024-11-07 19:44:28.741599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fb2501d54b4'
down_revision: Union[str, None] = '592bead63eb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('added_by', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'products', 'users', ['added_by'], ['id'])
    op.alter_column('users', 'type',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Enum('admin', 'user', name='userrole'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'type',
               existing_type=sa.Enum('admin', 'user', name='userrole'),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'added_by')
    # ### end Alembic commands ###