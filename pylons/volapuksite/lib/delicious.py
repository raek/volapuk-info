import threading
import time
import base64
import urllib
import urllib2
import xml.dom.minidom as minidom
from datetime import datetime

API_ROOT = "https://api.del.icio.us/v1"
# With a unique user agent string, we can be sure that if delicious bans us,
# they will ban only us and not all users of urllib.
USER_AGENT = "Volapuk.info-Bookmark-Fetcher/0.3"

DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

# To make sure that there will always be at least 2 seconds between api calls
# even in multithreaded programs.
api_lock = threading.Lock()

def make_request(request):
    # Wait 2 seconds and perform call.
    api_lock.acquire()
    time.sleep(2)
    try:
        response = urllib2.urlopen(request)
    finally:
        api_lock.release()
    return response

def api_call(credentials, api_method, params={}):
    url = "%s/%s?%s" % (API_ROOT, api_method, urllib.urlencode(params))
    request = urllib2.Request(url)
    request.add_header('User-Agent', USER_AGENT)
    #request.add_header('Referer', REFERER)
    credentials_b64 = base64.b64encode("%s:%s" % credentials)
    request.add_header('Authorization', "Basic %s" % credentials_b64)
    return make_request(request).read()

def get_last_updated(credentials):
    xml = api_call(credentials, "posts/update")
    xmldoc = minidom.parseString(xml)
    try:
        result = xmldoc.documentElement.attributes[u'time'].childNodes[0].data
        return datetime.strptime(result, DATE_FORMAT)
    finally:
        xmldoc.unlink()

# if a url_md5 is not in the keys, the bookmark has been deleted
# if the value for a key doesn't match the stored metadata md5, the bookmark has been changed
def get_change_manifest(credentials):
    xml = api_call(credentials, "posts/all", {'hashes': ""})
    xmldoc = minidom.parseString(xml)
    try:
        change_manifest = {}
        for post in xmldoc.getElementsByTagName('post'):
            url_md5 = post.attributes[u'url'].childNodes[0].data
            meta_md5 = post.attributes[u'meta'].childNodes[0].data
            change_manifest[url_md5] = meta_md5
        return change_manifest
    finally:
        xmldoc.unlink()

def parse_bookmarks(xmldoc):
    bookmarks = []
    for post in xmldoc.getElementsByTagName('post'):
        bookmark = {}
        bookmark['url'] = post.attributes[u'href'].childNodes[0].data
        bookmark['url_md5'] = post.attributes[u'hash'].childNodes[0].data
        bookmark['meta_md5'] = post.attributes[u'meta'].childNodes[0].data
        bookmark['title'] = post.attributes[u'description'].childNodes[0].data
        bookmark['description'] = post.attributes[u'extended'].childNodes[0].data
        bookmark['tags'] = post.attributes[u'tag'].childNodes[0].data
        bookmarks.append(bookmark)
    return bookmarks

def get_bookmarks_by_tags(credentials, tags):
    params = {'tag': tags.encode('utf-8'),
              'meta': 'yes'}
    xml = api_call(credentials, "posts/all", params)
    xmldoc = minidom.parseString(xml)
    try:
        return parse_bookmarks(xmldoc)
    finally:
        xmldoc.unlink()

def get_bookmarks_by_url_md5s(credentials, url_md5s):
    params = {'hashes': " ".join(url_md5s).encode('utf-8'),
              'meta': 'yes'}
    xml = api_call(credentials, "posts/get", params)
    xmldoc = minidom.parseString(xml)
    try:
        return parse_bookmarks(xmldoc)
    finally:
        xmldoc.unlink()

def get_bookmarks_from_date(credentials, from_date, tags=u""):
    params = {'fromdt': from_date.strftime(DATE_FORMAT),
              'tag': tags.encode('utf-8'),
              'meta': 'yes'}
    xml = api_call(credentials, "posts/all", params)
    xmldoc = minidom.parseString(xml)
    try:
        return parse_bookmarks(xmldoc)
    finally:
        xmldoc.unlink()

