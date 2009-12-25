"""The application's model objects"""
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import orm

from volapuksite.model import meta

from volapuksite.model.delicious_account import DeliciousAccount
from volapuksite.model.bookmark import Bookmark
from volapuksite.model.blog import Blog

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine



delicious_account_table = sa.Table('delicious_accounts', meta.metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    sa.Column('username', sa.types.String(64), unique=True),
    sa.Column('password', sa.types.String(64), nullable=False),
    sa.Column('required_tags', sa.types.String(256), nullable=False),
    sa.Column('last_updated', sa.types.DateTime, nullable=False))

bookmark_table = sa.Table('bookmarks', meta.metadata,
    sa.Column('account_id', sa.types.Integer, sa.ForeignKey('delicious_accounts.id'), nullable=False),
    sa.Column('url', sa.types.String(2048), nullable=False),
    sa.Column('url_md5', sa.types.String(32), nullable=False),
    sa.Column('meta_md5', sa.types.String(32), nullable=False),
    sa.Column('title', sa.types.String(256), nullable=False),
    sa.Column('description', sa.types.String(2048), nullable=False),
    sa.Column('tags', sa.types.String(256), nullable=False))

blog_table = sa.Table('blogs', meta.metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    sa.Column('feed_url', sa.types.String(2048), unique=True),
    sa.Column('title', sa.types.String(64), nullable=False),
    sa.Column('subtitle', sa.types.String(64), nullable=True),
    sa.Column('author', sa.types.String(64), nullable=False),
    sa.Column('last_updated', sa.types.DateTime, nullable=False))

orm.mapper(DeliciousAccount, delicious_account_table)
orm.mapper(Bookmark, bookmark_table,
    primary_key=[bookmark_table.c.account_id, bookmark_table.c.url_md5],
    properties={
        'account': orm.relation(DeliciousAccount, backref='bookmarks')})
orm.mapper(Blog, blog_table)



# These are the categories that appear on the learn page.
LINK_CATEGORIES = ['course', 'dictionary', 'grammar', 'website', 'reading', 'history', 'media']

