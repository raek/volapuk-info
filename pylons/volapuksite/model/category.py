import sqlalchemy as sa
from volapuksite.model import meta

category_table = sa.Table('categories', meta.metadata,
    sa.Column('tag', sa.types.String(256), primary_key=True),
    sa.Column('title', sa.types.String(256), nullable=False),
    sa.Column('order', sa.types.Integer, nullable=False))

class Category(object):
    
    def __init__(self, tag, title, order):
        self.tag = tag
        self.title = title
        self.order = order

