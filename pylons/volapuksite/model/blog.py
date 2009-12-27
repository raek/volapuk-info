from datetime import datetime
import sqlalchemy as sa
from volapuksite.model import meta

blog_table = sa.Table('blogs', meta.metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    sa.Column('feed_url', sa.types.String(2048), unique=True),
    sa.Column('title', sa.types.String(64), nullable=False),
    sa.Column('subtitle', sa.types.String(64), nullable=True),
    sa.Column('author', sa.types.String(64), nullable=False),
    sa.Column('last_updated', sa.types.DateTime, nullable=False))

class Blog(object):
    
    def __init__(self):
        self.last_updated = datetime.fromordinal(1)

