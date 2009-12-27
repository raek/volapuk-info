<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for('/')}">Volapük.info</a>
        → <a href="${h.url_for(controller='/admin')}">Admin</a>
        → <b>Bookmark Categories</b>
      </p>
</%def>
      <form method="POST" action="${h.url_for(action='save')}">
        <table>
          <tr><th>Order</th><th>Tag</th><th>Title</th><th>Delete?</th></tr>
          % for i, category in enumerate(c.categories):
          <tr>
            <td><input type="text" name="c${i}_order" value="${category.order}" size="3"></td>
            <td><input type="text" name="c${i}_tag" value="${category.tag}"></td>
            <td><input type="text" name="c${i}_title" value="${category.title}"></td>
            <td><input type="checkbox" name="c${i}_delete"></td>
          </tr>
          % endfor
          <tr>
            <td><input type="text" name="new_order" size="3"></td>
            <td><input type="text" name="new_tag"></td>
            <td><input type="text" name="new_title"></td>
            <td></td>
          </tr>
        </table>
        <p>
          <input type="hidden" name="count" value="${c.categories.count()}">
          <input type="submit" value="Save">
        </p>
      </form>
