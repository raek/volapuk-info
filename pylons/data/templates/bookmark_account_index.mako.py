from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261523564.7970819
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/bookmark_account_index.mako'
_template_uri='/bookmark_account_index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head']


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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n      <table>\n        <tr><th>Username</th><th>Last updated</th><th>Actions</th></tr>\n')
        # SOURCE LINE 5
        for account in c.accounts:
            # SOURCE LINE 6
            __M_writer(u'        <tr>\n          <td><a href="')
            # SOURCE LINE 7
            __M_writer(escape(h.url_for(action='view', id=account.id)))
            __M_writer(u'">')
            __M_writer(escape(account.username))
            __M_writer(u'</a></td>\n          <td>')
            # SOURCE LINE 8
            __M_writer(escape(account.last_updated))
            __M_writer(u'</td>\n          <td>\n            <a href="')
            # SOURCE LINE 10
            __M_writer(escape(h.url_for(action='view', id=account.id)))
            __M_writer(u'">View</a>\n            <a href="')
            # SOURCE LINE 11
            __M_writer(escape(h.url_for(action='edit', id=account.id)))
            __M_writer(u'">Edit</a>\n            <input type="submit" value="Delete...">\n            <input type="submit" value="Check for updates...">\n          </td>\n        </tr>\n')
        # SOURCE LINE 17
        __M_writer(u'      </table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


