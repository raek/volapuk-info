from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261601110.079663
_template_filename='/home/raek/Projekt/volapuk-info/pylons/volapuksite/templates/base/vp-base.mako'
_template_uri='/base/vp-base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['breadcrumb', 'head']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n<!doctype html> \n<html>\n  <head>\n    <title>Volap\xfck.info \u2013 ')
        # SOURCE LINE 6
        __M_writer(escape(c.title))
        __M_writer(u'</title>\n    <meta charset="utf-8">\n    <link rel="stylesheet" type="text/css" href="/styles/telid.css">\n    ')
        # SOURCE LINE 9
        __M_writer(escape(self.head()))
        __M_writer(u'\n  </head>\n  <body>\n    <div id="header">\n      <div class="logo">Volap\xfck.info</div>\n      <a class="nav_link" id="bal" href="/front">\n        <div class="title">Home</div>\n        <div class="desc">Introduction to the <br> Volap\xfck language</div>\n      </a>\n      <a class="nav_link" id="tel" href="/learn">\n        <div class="title">Learn</div>\n        <div class="desc">Courses, grammars, <br> dictionaries, etc</div>\n      </a>\n      <a class="nav_link" id="kil" href="/blogs">\n        <div class="title">Read</div>\n        <div class="desc">Blogs in and about <br> Volap\xfck</div>\n      </a>\n      <a class="nav_link" id="fol" href="/social">\n        <div class="title">Speak</div>\n        <div class="desc">Where to get in <br> touch with Volap\xfck</div>\n      </a>\n    </div>\n    <div id="breadcrumb">\n      ')
        # SOURCE LINE 32
        __M_writer(escape(self.breadcrumb()))
        __M_writer(u'\n    </div>\n    <div id="main">\n      <h1>')
        # SOURCE LINE 35
        __M_writer(escape(c.title))
        __M_writer(u'</h1>\n      ')
        # SOURCE LINE 36
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </div>\n    <div id="footer">&nbsp;\n    </div>\n  </body>\n</html>\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumb(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
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


