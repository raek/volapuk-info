from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261525059.6308579
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/component/breadcrumb.mako'
_template_uri='/component/breadcrumb.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'      <div class="breadcrumb">\n        <a href="')
        # SOURCE LINE 2
        __M_writer(escape(h.url_for(controller='/admin')))
        __M_writer(u'">Admin</a>\n      </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


