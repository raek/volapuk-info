from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261612302.241498
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/blog_index.mako'
_template_uri='/blog_index.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n      <table>\n        <tr><th>id</th><th>title</th><th>last updated</th><th>actions</th></tr>\n')
        # SOURCE LINE 10
        for blog in c.blogs:
            # SOURCE LINE 11
            __M_writer(u'        <tr>\n          <td>')
            # SOURCE LINE 12
            __M_writer(escape(blog.id))
            __M_writer(u'</td>\n          <td>')
            # SOURCE LINE 13
            __M_writer(escape(blog.title))
            __M_writer(u'</td>\n          <td>')
            # SOURCE LINE 14
            __M_writer(escape(blog.last_updated))
            __M_writer(u'</td>\n          <td>[show] [edit] [delete] [fetch posts]</td>\n        </tr>\n')
        # SOURCE LINE 18
        __M_writer(u'      </table>\n')
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
        __M_writer(u'">Admin</a>\n        \u2192 <b>Blogs</b>\n      </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


