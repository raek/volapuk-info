<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for('/')}">Volapük.info</a>
        → <a href="${h.url_for(controller='/admin')}">Admin</a>
        → <b>Blogs</b>
      </p>
</%def>
      <table>
        <tr><th>id</th><th>title</th><th>last updated</th><th>actions</th></tr>
        % for blog in c.blogs:
        <tr>
          <td>${blog.id}</td>
          <td>${blog.title}</td>
          <td>${blog.last_updated}</td>
          <td>[show] [edit] [delete] [fetch posts]</td>
        </tr>
        % endfor
      </table>
