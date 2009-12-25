<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <b>Volapük.info</b>
      </p>
</%def>
<%def name="sidebar()">
      <h2>News</h2>
      <ul>
        % for tag in c.tags:
        <li><a href="${h.url_for(action='by_tag', id=tag)}">${tag}</a></li>
        % endfor
      </ul>
</%def>
      <p>A big long text</p>
