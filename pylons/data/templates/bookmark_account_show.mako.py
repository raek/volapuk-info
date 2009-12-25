from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261524292.0994849
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/bookmark_account_show.mako'
_template_uri='/bookmark_account_show.mako'
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
        __M_writer(u'\n')
        # SOURCE LINE 3
        runtime._include_file(context, '/component/breadcrumb.mako', _template_uri)
        __M_writer(u'\n      <table class="vertical">\n        <tr>\n          <th>username</th>\n')
        # SOURCE LINE 7
        if c.edit:
            # SOURCE LINE 8
            __M_writer(u'          <td><input type="text" name="username" value="')
            __M_writer(escape(c.account.username))
            __M_writer(u'"></td>\n')
            # SOURCE LINE 9
        else:
            # SOURCE LINE 10
            __M_writer(u'          <td>')
            __M_writer(escape(c.account.username))
            __M_writer(u'</td>\n')
        # SOURCE LINE 12
        __M_writer(u'        </tr>\n        <tr>\n          <th>password</th>\n')
        # SOURCE LINE 15
        if c.edit:
            # SOURCE LINE 16
            __M_writer(u'          <td><input type="password" name="password"></td>\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'          <td>********</td>\n')
        # SOURCE LINE 20
        __M_writer(u'        </tr>\n        <tr>\n          <th>last updated</th>\n          <td>')
        # SOURCE LINE 23
        __M_writer(escape(c.account.last_updated))
        __M_writer(u'</td>\n        </tr>\n        <tr>\n          <th>actions</th>\n          <td>\n')
        # SOURCE LINE 28
        if c.edit:
            # SOURCE LINE 29
            __M_writer(u'            <a href="')
            __M_writer(escape(h.url_for(action='view', id=c.account.id)))
            __M_writer(u'">View</a>\n')
            # SOURCE LINE 30
        else:
            # SOURCE LINE 31
            __M_writer(u'            <a href="')
            __M_writer(escape(h.url_for(action='edit', id=c.account.id)))
            __M_writer(u'">Edit</a>\n')
        # SOURCE LINE 33
        __M_writer(u'            <input type="submit" value="Delete...">\n            <input type="submit" value="Check for updates...">\n          </td>\n        </tr>\n      </table>\n')
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


