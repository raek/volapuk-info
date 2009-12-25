# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from volapuksite.lib.base import BaseController, render
from volapuksite.model import meta, DeliciousAccount

log = logging.getLogger(__name__)

class DeliciousAccountController(BaseController):

    def index(self):
        c.title = "Delicious Accounts"
        c.accounts = meta.Session.query(DeliciousAccount).order_by(DeliciousAccount.username)
        return render("/derived/delicious_index.mako")
    
    def new(self):
        c.title = u"New Delicious Account"
        c.mode = 'new'
        return render("/derived/delicious_account.mako")
    
    def create(self):
        if request.method != 'POST':
            abort(405)
        username = request.params['username']
        password = request.params['password']
        required_tags = request.params['required_tags']
        account = DeliciousAccount(username, password, required_tags)
        meta.Session.add(account)
        account.clean_update()
        meta.Session.commit()
        redirect_to(action='view', id=account.id)
    
    def view(self, id):
        c.account = meta.Session.query(DeliciousAccount).get(int(id))
        c.title = u"Delicious Account “" + c.account.username + u"”"
        c.mode = 'view'
        return render("/derived/delicious_account.mako")
    
    def edit(self, id):
        c.account = meta.Session.query(DeliciousAccount).get(int(id))
        c.title = u"Editing Delicious Account “" + c.account.username + u"”"
        c.mode = 'edit'
        return render("/derived/delicious_account.mako")
    
    def update(self, id):
        if request.method != 'POST':
            abort(405)
        account = meta.Session.query(DeliciousAccount).get(int(id))
        username = request.params['username']
        password = request.params['password']
        required_tags = request.params['required_tags']
        account.username = username
        account.password = password
        if account.required_tags != required_tags:
            account.required_tags = required_tags
            account.clean_update()
        else:
            account.required_tags = required_tags
        meta.Session.commit()
        redirect_to(action='view')
    
    def update_bookmarks(self, id):
        if request.method != 'POST':
            abort(405)
        account = meta.Session.query(DeliciousAccount).get(int(id))
        account.update()
        meta.Session.commit()
        redirect_to(action='view', id=account.id)
    
    def delete(self, id):
        if request.method != 'POST':
            abort(405)
        account = meta.Session.query(DeliciousAccount).get(int(id))
        account.clear()
        meta.Session.delete(account)
        meta.Session.commit()
        redirect_to(action='index')
    
    def clear(self, id):
        account = meta.Session.query(DeliciousAccount).get(int(id))
        account.clear()
        meta.Session.commit()


