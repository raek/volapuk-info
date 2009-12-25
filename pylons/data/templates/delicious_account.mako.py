from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261612236.3205111
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/delicious_account.mako'
_template_uri='/delicious_account.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['breadcrumb']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/vp-base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n      <table class="vertical">\n        <tr>\n          <th>Username</th>\n')
        # SOURCE LINE 12
        if c.edit:
            # SOURCE LINE 13
            __M_writer(u'          <td><input type="text" name="username" value="')
            __M_writer(escape(c.account.username))
            __M_writer(u'"></td>\n')
            # SOURCE LINE 14
        else:
            # SOURCE LINE 15
            __M_writer(u'          <td>')
            __M_writer(escape(c.account.username))
            __M_writer(u'</td>\n')
        # SOURCE LINE 17
        __M_writer(u'        </tr>\n        <tr>\n          <th>Password</th>\n')
        # SOURCE LINE 20
        if c.edit:
            # SOURCE LINE 21
            __M_writer(u'          <td><input type="password" name="password"></td>\n')
            # SOURCE LINE 22
        else:
            # SOURCE LINE 23
            __M_writer(u'          <td><i>(hidden)</i><td>\n')
        # SOURCE LINE 25
        __M_writer(u'        </tr>\n        <tr>\n          <th>Bookmarks</th>\n          <td>')
        # SOURCE LINE 28
        __M_writer(escape(len(c.account.bookmarks)))
        __M_writer(u'</td>\n        </tr>\n        <tr>\n          <th>Last checked</th>\n          <td>')
        # SOURCE LINE 32
        __M_writer(escape(h.time_ago_in_words(c.account.last_checked, 'hour')))
        __M_writer(u' ago</td>\n        </tr>\n        <tr>\n          <th>Actions</th>\n          <td>\n')
        # SOURCE LINE 37
        if c.edit:
            # SOURCE LINE 38
            __M_writer(u'            <a href="')
            __M_writer(escape(h.url_for(action='view', id=c.account.id)))
            __M_writer(u'">View</a>\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            __M_writer(u'            <a href="')
            __M_writer(escape(h.url_for(action='edit', id=c.account.id)))
            __M_writer(u'">Edit</a>\n')
        # SOURCE LINE 42
        __M_writer(u'            <form method="POST" action="')
        __M_writer(escape(h.url_for(action='delete', id=c.account.id)))
        __M_writer(u'">\n              <input type="submit" value="Delete...">\n            </form>\n            <form method="POST" action="')
        # SOURCE LINE 45
        __M_writer(escape(h.url_for(action='update', id=c.account.id)))
        __M_writer(u'">\n              <input type="submit" value="Check for updates...">\n            </form>\n          </td>\n        </tr>\n      </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumb(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n      <p>\n        <a href="')
        # SOURCE LINE 4
        __M_writer(escape(h.url_for(controller='/admin')))
        __M_writer(u'">Admin</a>\n        \u2192 <a href="')
        # SOURCE LINE 5
        __M_writer(escape(h.url_for(action='index')))
        __M_writer(u'">Delicous Accounts</a>\n        \u2192 <b>')
        # SOURCE LINE 6
        __M_writer(escape(c.account.username))
        __M_writer(u'</b>\n      </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


