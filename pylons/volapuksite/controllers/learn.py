# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render
from volapuksite.model import meta, Bookmark, Category

log = logging.getLogger(__name__)

TAGS = ["course", "dictionary", "grammar", "website", "media", "reading", "history"]

class LearnController(BaseController):

    def index(self):
        c.title = "Learning Resources"
        c.categories = meta.Session.query(Category).order_by(Category.order)
        return render("/derived/resource_index.mako")
    
    def category(self, id):
        c.category = meta.Session.query(Category).get(id)
        c.title = c.category.title
        c.categories = meta.Session.query(Category).order_by(Category.order)
        c.bookmarks = meta.Session.query(Bookmark).filter(Bookmark.tags.like("%" + id + "%")).order_by(Bookmark.title)
        return render("/derived/resource_category.mako")
