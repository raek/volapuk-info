<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for(controller='/admin')}">Admin</a>
        → <b>Delicous Accounts</b>
      </p>
</%def>
      <table>
        <tr><th>Username</th><th>Count</th><th>Last updated</th><th>Actions</th></tr>
        % for account in c.accounts:
        <tr>
          <td><a href="${h.url_for(action='view', id=account.id)}">${account.username}</a></td>
          <td>${len(account.bookmarks)}</td>
          <td>${h.time_ago_in_words(account.last_updated, 'day')} ago</td>
          <td>
            <a href="${h.url_for(action='view', id=account.id)}">View</a>
            <a href="${h.url_for(action='edit', id=account.id)}">Edit</a>
            <form method="POST" action="${h.url_for(action='delete', id=account.id)}">
              <input type="submit" value="Delete">
            </form>
            <form method="POST" action="${h.url_for(action='update_bookmarks', id=account.id)}">
              <input type="submit" value="Check for updates">
            </form>
          </td>
        </tr>
        % endfor
      </table>
      <p><a href="${h.url_for(action='new')}">New delicious account</a></p>
