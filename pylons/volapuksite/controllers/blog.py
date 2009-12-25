import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render
from volapuksite.model import meta, Blog

log = logging.getLogger(__name__)

class BlogController(BaseController):

    def index(self):
        c.title = "Blogs"
        c.blogs = meta.Session.query(Blog)
        return render("/blog_index.mako")
