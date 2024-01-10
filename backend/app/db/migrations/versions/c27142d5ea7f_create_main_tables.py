"""create_main_tables
 
Revision ID: c27142d5ea7f
Revises: 
Create Date: 2024-01-09 13:35:09.922399
 
"""
from alembic import op
import sqlalchemy as sa

 
# revision identifiers, used by Alembic
revision = 'c27142d5ea7f'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("address", sa.Text, nullable=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )
 
 
def upgrade() -> None:
    pass
 
 
def downgrade() -> None:
    pass