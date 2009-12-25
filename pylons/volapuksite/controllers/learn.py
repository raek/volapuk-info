# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render
from volapuksite.model import meta, Bookmark

log = logging.getLogger(__name__)

TAGS = ["course", "dictionary", "grammar", "website", "media", "reading", "history"]

class LearnController(BaseController):

    def index(self):
        c.title = "Learn"
        c.categories = TAGS
        return render("/derived/resource_index.mako")
    
    def category(self, id):
        c.category = id
        c.title = u"Category: " + id
        c.categories = TAGS
        c.bookmarks = meta.Session.query(Bookmark).filter(Bookmark.tags.like("%" + id + "%")).order_by(Bookmark.title)
        return render("/derived/resource_category.mako")
