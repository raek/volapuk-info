from datetime import datetime, timedelta
import sqlalchemy as sa
from volapuksite.lib import delicious as d
from volapuksite.model import meta
from volapuksite.model.bookmark import Bookmark

delicious_account_table = sa.Table('delicious_accounts', meta.metadata,
    sa.Column('id', sa.types.Integer, primary_key=True),
    sa.Column('username', sa.types.String(64), unique=True),
    sa.Column('password', sa.types.String(64), nullable=False),
    sa.Column('required_tags', sa.types.String(256), nullable=False),
    sa.Column('last_updated', sa.types.DateTime, nullable=False))

class DeliciousAccount(object):
    
    def __init__(self, username, password, required_tags=""):
        self.username = username
        self.password = password
        self.required_tags = required_tags
        self.last_updated = datetime(1900, 1, 1)
    
    @property
    def credentials(self):
        return (self.username, self.password)
    
    def add_bookmarks_from_delicious(self, bookmarks):
        added = []
        for bookmark in bookmarks:
            new_bookmark = Bookmark.from_delicious(self, bookmark)
            added.append(new_bookmark)
            meta.Session.add(new_bookmark)
        return added
    
    # Synchronize the bookmarks with delicous.com. This returns a three-tuple
    # of the added, updated and deleted bookmarks.
    def update(self):
        # Check if any changes has been made
        bookmarks_last_updated = d.get_last_updated(self.credentials)
        if bookmarks_last_updated <= self.last_updated:
            return ([], [], [])
        
        # A dictionary of all the bookmarks that should be updated. The keys are
        # the URL MD5s and the values are the bookmarks themselves.
        updated_url_md5s = []
        
        deleted = []
        updated = []
        if self.bookmarks:
            # Look for deleted or changed bookmarks. Deleted bookmarks are removed
            # from the local database if not found in the change manifest. URL MD5s
            # of the changed bookmarks are stored and the (now outdated) bookmarks
            # are deleted.
            change_manifest = d.get_change_manifest(self.credentials)
            for bookmark in self.bookmarks:
                if bookmark.url_md5 in change_manifest:
                    if bookmark.meta_md5 != change_manifest[bookmark.url_md5]:
                        # The bookmark has been changed
                        updated_url_md5s.append(bookmark.url_md5)
                        meta.Session.delete(bookmark)
                else:
                    # The bookmark has been deleted
                    deleted.append(bookmark)
                    meta.Session.delete(bookmark)
            
            # Fetch new versions of the changed bookmarks
            if updated_url_md5s:
                bookmarks = d.get_bookmarks_by_url_md5s(self.credentials, updated_url_md5s)
                updated = self.add_bookmarks_from_delicious(bookmarks)
        
        # Fetch any new bookmarks
        # Add one second to the time of the last bookmark to not get that again.
        from_time = self.last_updated + timedelta(seconds=1)
        bookmarks = d.get_bookmarks_from_date(self.credentials, from_time, self.required_tags)
        added = self.add_bookmarks_from_delicious(bookmarks)
        
        self.last_updated = bookmarks_last_updated
        return (added, updated, deleted)
    
    def clean_update(self):
        for bookmark in self.bookmarks:
            meta.Session.delete(bookmark)
        new_bookmarks = d.get_bookmarks_by_tags(self.credentials,
                                                self.required_tags)
        for bookmark in new_bookmarks:
            meta.Session.add(Bookmark.from_delicious(self, bookmark))
        self.last_updated = datetime.now()
    
    def clear(self):
        for bookmark in self.bookmarks:
            meta.Session.delete(bookmark)

