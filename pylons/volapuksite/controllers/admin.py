import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def index(self):
        return render('/derived/admin.mako')
