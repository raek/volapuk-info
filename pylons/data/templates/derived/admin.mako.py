from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261614312.90184
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/derived/admin.mako'
_template_uri='/derived/admin.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n      <ul>\n        <li><a href="')
        # SOURCE LINE 8
        __M_writer(escape(h.url_for(controller='/delicious_account')))
        __M_writer(u'">Delicious Accounts</a></li>\n        <li><a href="')
        # SOURCE LINE 9
        __M_writer(escape(h.url_for(controller='/blog')))
        __M_writer(u'">Blogs</a></li>\n        <li><a href="')
        # SOURCE LINE 10
        __M_writer(escape(h.url_for(controller='/twitter_hashtag')))
        __M_writer(u'">Twitter Hashtag</a></li>\n      </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumb(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n      <p>\n        <b>Admin</b>\n      </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


