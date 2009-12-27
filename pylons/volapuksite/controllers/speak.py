import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SpeakController(BaseController):

    def index(self):
        redirect_to("http://embed.mibbit.com/?server=irc.unilang.org&channel=%23volapuk")
