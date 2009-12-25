<%inherit file="/base/resources.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for('/')}">Volapük.info</a>
        → <a href="${h.url_for(controller='/learn')}">Learn</a>
        → <b>Tag: ${c.tag}</b>
      </p>
</%def>
      <dl>
        % for bookmark in c.bookmarks:
        <dt><a href="${bookmark.url}">${bookmark.title}</a></dt>
        <dd>${bookmark.description}</dd>
        % endfor
      </dl>
