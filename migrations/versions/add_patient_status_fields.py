"""Add patient status and priority fields

Revision ID: add_patient_status_fields
Revises: a581d5aab34d
Create Date: 2025-10-26 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_patient_status_fields'
down_revision = 'a581d5aab34d'
branch_labels = None
depends_on = None

def upgrade():
    # Add new columns to patient table
    op.add_column('patient', sa.Column('status', sa.String(length=20), nullable=True))
    op.add_column('patient', sa.Column('priority', sa.String(length=20), nullable=True))
    op.add_column('patient', sa.Column('medical_notes', sa.Text(), nullable=True))
    op.add_column('patient', sa.Column('updated_at', sa.DateTime(), nullable=True))
    
    # Set default values for existing records
    op.execute("UPDATE patient SET status = 'active' WHERE status IS NULL")
    op.execute("UPDATE patient SET priority = 'medium' WHERE priority IS NULL")
    op.execute("UPDATE patient SET updated_at = created_at WHERE updated_at IS NULL")

def downgrade():
    # Remove the columns
    op.drop_column('patient', 'updated_at')
    op.drop_column('patient', 'medical_notes')
    op.drop_column('patient', 'priority')
    op.drop_column('patient', 'status')