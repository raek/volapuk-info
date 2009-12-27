import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render
from volapuksite.model import meta, Category

log = logging.getLogger(__name__)

class CategoryController(BaseController):

    def index(self):
        c.title = "Bookmark Categories"
        c.categories = meta.Session.query(Category).order_by(Category.order)
        return render("/derived/categories.mako")
    
    def save(self):
        for category in meta.Session.query(Category):
            meta.Session.delete(category)
        for i in range(int(request.params['count'])):
            prefix = "c{0}_".format(i)
            tag = request.params[prefix + 'tag']
            title = request.params[prefix + 'title']
            order = request.params[prefix + 'order']
            if prefix + 'delete' not in request.params:
                category = Category(tag, title, order)
                meta.Session.add(category)
        if request.params.get('new_tag', None):
            prefix = "new_"
            tag = request.params[prefix + 'tag']
            title = request.params[prefix + 'title']
            order = request.params[prefix + 'order']
            category = Category(tag, title, order)
            meta.Session.add(category)
        meta.Session.commit()
        redirect_to(action='index')
