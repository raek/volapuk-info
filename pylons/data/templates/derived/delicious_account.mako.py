from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261761642.5335579
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/derived/delicious_account.mako'
_template_uri='/derived/delicious_account.mako'
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
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        if c.mode == 'new':
            # SOURCE LINE 14
            __M_writer(u'      <form method="POST" action="')
            __M_writer(escape(h.url_for(action='create', id=None)))
            __M_writer(u'">\n')
            # SOURCE LINE 15
        elif c.mode == 'edit':
            # SOURCE LINE 16
            __M_writer(u'      <form method="POST" action="')
            __M_writer(escape(h.url_for(action='update')))
            __M_writer(u'">\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'      <div>\n')
        # SOURCE LINE 20
        __M_writer(u'        <table class="vertical">\n          <tr>\n            <th>Username</th>\n')
        # SOURCE LINE 23
        if c.mode == 'view':
            # SOURCE LINE 24
            __M_writer(u'            <td>')
            __M_writer(escape(c.account.username))
            __M_writer(u'</td>\n')
            # SOURCE LINE 25
        elif c.mode == 'edit':
            # SOURCE LINE 26
            __M_writer(u'            <td><input type="text" name="username" value="')
            __M_writer(escape(c.account.username))
            __M_writer(u'"></td>\n')
            # SOURCE LINE 27
        else:
            # SOURCE LINE 28
            __M_writer(u'            <td><input type="text" name="username"></td>\n')
        # SOURCE LINE 30
        __M_writer(u'          </tr>\n          <tr>\n            <th>Password</th>\n')
        # SOURCE LINE 33
        if c.mode == 'view':
            # SOURCE LINE 34
            __M_writer(u'            <td><i>(hidden)</i><td>\n')
            # SOURCE LINE 35
        else:
            # SOURCE LINE 36
            __M_writer(u'            <td><input type="password" name="password"></td>\n')
        # SOURCE LINE 38
        __M_writer(u'          </tr>\n          <tr>\n            <th>Filter tags</th>\n')
        # SOURCE LINE 41
        if c.mode == 'view':
            # SOURCE LINE 42
            __M_writer(u'            <td>')
            __M_writer(escape(c.account.required_tags))
            __M_writer(u'</td>\n')
            # SOURCE LINE 43
        elif c.mode == 'edit':
            # SOURCE LINE 44
            __M_writer(u'            <td><input type="text" name="required_tags" value="')
            __M_writer(escape(c.account.required_tags))
            __M_writer(u'"></td>\n')
            # SOURCE LINE 45
        else:
            # SOURCE LINE 46
            __M_writer(u'            <td><input type="text" name="required_tags"></td>\n')
        # SOURCE LINE 48
        __M_writer(u'          </tr>\n')
        # SOURCE LINE 49
        if c.mode == 'new':
            # SOURCE LINE 50
            __M_writer(u'          <tr>\n            <th></th>\n            <td class="submit"><input type="submit" value="Create"></td>\n          </tr>\n')
            # SOURCE LINE 54
        elif c.mode == 'edit':
            # SOURCE LINE 55
            __M_writer(u'          <tr>\n            <th></th>\n            <td class="submit"><a href="')
            # SOURCE LINE 57
            __M_writer(escape(h.url_for(action='view')))
            __M_writer(u'">Cancel</a> <input type="submit" value="Save"></td>\n          </tr>\n')
            # SOURCE LINE 59
        else:
            # SOURCE LINE 60
            __M_writer(u'          <tr>\n            <th>Bookmarks</th>\n            <td>')
            # SOURCE LINE 62
            __M_writer(escape(len(c.account.bookmarks)))
            __M_writer(u'</td>\n          </tr>\n          <tr>\n            <th>Last updated</th>\n            <td>')
            # SOURCE LINE 66
            __M_writer(escape(h.time_ago_in_words(c.account.last_updated, 'day')))
            __M_writer(u' ago</td>\n          </tr>\n          <tr>\n            <th>Actions</th>\n            <td>\n')
            # SOURCE LINE 71
            if c.edit:
                # SOURCE LINE 72
                __M_writer(u'              <a href="')
                __M_writer(escape(h.url_for(action='view', id=c.account.id)))
                __M_writer(u'">View</a>\n')
                # SOURCE LINE 73
            else:
                # SOURCE LINE 74
                __M_writer(u'              <a href="')
                __M_writer(escape(h.url_for(action='edit', id=c.account.id)))
                __M_writer(u'">Edit</a>\n')
            # SOURCE LINE 76
            __M_writer(u'              <form method="POST" action="')
            __M_writer(escape(h.url_for(action='delete', id=c.account.id)))
            __M_writer(u'">\n                <input type="submit" value="Delete">\n              </form>\n              <form method="POST" action="')
            # SOURCE LINE 79
            __M_writer(escape(h.url_for(action='update_bookmarks', id=c.account.id)))
            __M_writer(u'">\n                <input type="submit" value="Check for updates">\n              </form>\n            </td>\n          </tr>\n')
        # SOURCE LINE 85
        __M_writer(u'        </table>\n')
        # SOURCE LINE 86
        if c.mode == 'view':
            # SOURCE LINE 87
            __M_writer(u'      </div>\n')
            # SOURCE LINE 88
        else:
            # SOURCE LINE 89
            __M_writer(u'      </form>\n')
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
        __M_writer(escape(h.url_for(action='index', id=None)))
        __M_writer(u'">Delicous Accounts</a>\n')
        # SOURCE LINE 6
        if c.mode == 'new':
            # SOURCE LINE 7
            __M_writer(u'        \u2192 <b>New</b>\n')
            # SOURCE LINE 8
        else:
            # SOURCE LINE 9
            __M_writer(u'        \u2192 <b>')
            __M_writer(escape(c.account.username))
            __M_writer(u'</b>\n')
        # SOURCE LINE 11
        __M_writer(u'      </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


