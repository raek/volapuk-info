# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ReadController(BaseController):

    def index(self):
        return u"I'm working on it! // Räk"
