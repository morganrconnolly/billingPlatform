"""empty message

Revision ID: 232a0c5a78ff
Revises: e70bd0375be8
Create Date: 2016-07-20 12:58:11.691851

"""

# revision identifiers, used by Alembic.
revision = '232a0c5a78ff'
down_revision = 'e70bd0375be8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('group_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'student_group_fkey', 'student', type_='foreignkey')
    op.create_foreign_key(None, 'student', 'group', ['group_id'], ['id'])
    op.drop_column('student', 'group')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('group', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.create_foreign_key(u'student_group_fkey', 'student', 'group', ['group'], ['id'])
    op.drop_column('student', 'group_id')
    ### end Alembic commands ###
