import sqlalchemy as sa
from volapuksite.model import meta

bookmark_table = sa.Table('bookmarks', meta.metadata,
    sa.Column('account_id', sa.types.Integer, sa.ForeignKey('delicious_accounts.id'), nullable=False),
    sa.Column('url', sa.types.String(2048), nullable=False),
    sa.Column('url_md5', sa.types.String(32), nullable=False),
    sa.Column('meta_md5', sa.types.String(32), nullable=False),
    sa.Column('title', sa.types.String(256), nullable=False),
    sa.Column('description', sa.types.String(2048), nullable=False),
    sa.Column('tags', sa.types.String(256), nullable=False))

class Bookmark(object):
    
    def __init__(self, account, url, url_md5, meta_md5, title, description, tags):
        self.account = account
        self.url = url
        self.url_md5 = url_md5
        self.meta_md5 = meta_md5
        self.tags = tags
        self.title = title
        self.description = description
    
    @staticmethod
    def from_delicious(account, bookmark):
        return Bookmark(account,
                        bookmark['url'],
                        bookmark['url_md5'],
                        bookmark['meta_md5'],
                        bookmark['title'],
                        bookmark['description'],
                        bookmark['tags'])

