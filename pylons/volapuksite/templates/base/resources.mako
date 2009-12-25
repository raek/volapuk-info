<%inherit file="/base/vp-base.mako" />
<%def name="sidebar()">
      <h2>Categories</h2>
      <ul>
        % for category in c.categories:
        <li><a href="${h.url_for(action='category', id=category)}">${category}</a></li>
        % endfor
      </ul>
</%def>
