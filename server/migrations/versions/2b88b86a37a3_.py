"""empty message

Revision ID: 2b88b86a37a3
Revises: 5d9646c6c5f8
Create Date: 2016-07-19 14:39:46.601826

"""

# revision identifiers, used by Alembic.
revision = '2b88b86a37a3'
down_revision = '5d9646c6c5f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    ### end Alembic commands ###
