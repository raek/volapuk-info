"""The application's model objects"""
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import orm

from volapuksite.model import meta

from volapuksite.model.delicious_account import delicious_account_table, DeliciousAccount
from volapuksite.model.bookmark import bookmark_table, Bookmark
from volapuksite.model.blog import blog_table, Blog
from volapuksite.model.category import category_table, Category

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

orm.mapper(DeliciousAccount, delicious_account_table)
orm.mapper(Bookmark, bookmark_table,
    primary_key=[bookmark_table.c.account_id, bookmark_table.c.url_md5],
    properties={
        'account': orm.relation(DeliciousAccount, backref='bookmarks')})
orm.mapper(Blog, blog_table)
orm.mapper(Category, category_table)

