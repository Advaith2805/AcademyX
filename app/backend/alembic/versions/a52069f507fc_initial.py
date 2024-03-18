"""Initial

Revision ID: a52069f507fc
Revises: 
Create Date: 2024-03-18 18:41:01.093522

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a52069f507fc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('length_words', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_article_id'), 'article', ['id'], unique=False)
    op.create_index(op.f('ix_article_title'), 'article', ['title'], unique=False)
    op.create_index(op.f('ix_article_url'), 'article', ['url'], unique=False)
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('image_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('estimated_time_hrs', sa.Float(), nullable=True),
    sa.Column('avg_rating', sa.Float(), nullable=True),
    sa.Column('published', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_id'), 'course', ['id'], unique=False)
    op.create_index(op.f('ix_course_title'), 'course', ['title'], unique=False)
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('estimated_time_minutes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lesson_id'), 'lesson', ['id'], unique=False)
    op.create_index(op.f('ix_lesson_title'), 'lesson', ['title'], unique=False)
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('estimated_time_minutes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_module_id'), 'module', ['id'], unique=False)
    op.create_index(op.f('ix_module_title'), 'module', ['title'], unique=False)
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_image', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('avatar_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('joined_at', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('length_minutes', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_video_id'), 'video', ['id'], unique=False)
    op.create_index(op.f('ix_video_title'), 'video', ['title'], unique=False)
    op.create_index(op.f('ix_video_url'), 'video', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_url'), table_name='video')
    op.drop_index(op.f('ix_video_title'), table_name='video')
    op.drop_index(op.f('ix_video_id'), table_name='video')
    op.drop_table('video')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    op.drop_index(op.f('ix_module_title'), table_name='module')
    op.drop_index(op.f('ix_module_id'), table_name='module')
    op.drop_table('module')
    op.drop_index(op.f('ix_lesson_title'), table_name='lesson')
    op.drop_index(op.f('ix_lesson_id'), table_name='lesson')
    op.drop_table('lesson')
    op.drop_index(op.f('ix_course_title'), table_name='course')
    op.drop_index(op.f('ix_course_id'), table_name='course')
    op.drop_table('course')
    op.drop_index(op.f('ix_article_url'), table_name='article')
    op.drop_index(op.f('ix_article_title'), table_name='article')
    op.drop_index(op.f('ix_article_id'), table_name='article')
    op.drop_table('article')
    # ### end Alembic commands ###
