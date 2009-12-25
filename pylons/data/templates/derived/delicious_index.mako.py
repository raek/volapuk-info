from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261761659.3831351
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/derived/delicious_index.mako'
_template_uri='/derived/delicious_index.mako'
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
        # SOURCE LINE 7
        __M_writer(u'\n      <table>\n        <tr><th>Username</th><th>Count</th><th>Last updated</th><th>Actions</th></tr>\n')
        # SOURCE LINE 10
        for account in c.accounts:
            # SOURCE LINE 11
            __M_writer(u'        <tr>\n          <td><a href="')
            # SOURCE LINE 12
            __M_writer(escape(h.url_for(action='view', id=account.id)))
            __M_writer(u'">')
            __M_writer(escape(account.username))
            __M_writer(u'</a></td>\n          <td>')
            # SOURCE LINE 13
            __M_writer(escape(len(account.bookmarks)))
            __M_writer(u'</td>\n          <td>')
            # SOURCE LINE 14
            __M_writer(escape(h.time_ago_in_words(account.last_updated, 'day')))
            __M_writer(u' ago</td>\n          <td>\n            <a href="')
            # SOURCE LINE 16
            __M_writer(escape(h.url_for(action='view', id=account.id)))
            __M_writer(u'">View</a>\n            <a href="')
            # SOURCE LINE 17
            __M_writer(escape(h.url_for(action='edit', id=account.id)))
            __M_writer(u'">Edit</a>\n            <form method="POST" action="')
            # SOURCE LINE 18
            __M_writer(escape(h.url_for(action='delete', id=account.id)))
            __M_writer(u'">\n              <input type="submit" value="Delete">\n            </form>\n            <form method="POST" action="')
            # SOURCE LINE 21
            __M_writer(escape(h.url_for(action='update_bookmarks', id=account.id)))
            __M_writer(u'">\n              <input type="submit" value="Check for updates">\n            </form>\n          </td>\n        </tr>\n')
        # SOURCE LINE 27
        __M_writer(u'      </table>\n      <p><a href="')
        # SOURCE LINE 28
        __M_writer(escape(h.url_for(action='new')))
        __M_writer(u'">New delicious account</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumb(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n      <p>\n        <a href="')
        # SOURCE LINE 4
        __M_writer(escape(h.url_for(controller='/admin')))
        __M_writer(u'">Admin</a>\n        \u2192 <b>Delicous Accounts</b>\n      </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


