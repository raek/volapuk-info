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

