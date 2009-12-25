<%inherit file="/base/vp-base.mako"/>
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for(controller='/admin')}">Admin</a>
        → <a href="${h.url_for(action='index', id=None)}">Delicous Accounts</a>
        % if c.mode == 'new':
        → <b>New</b>
        % else:
        → <b>${c.account.username}</b>
        % endif
      </p>
</%def>
      % if c.mode == 'new':
      <form method="POST" action="${h.url_for(action='create', id=None)}">
      % elif c.mode == 'edit':
      <form method="POST" action="${h.url_for(action='update')}">
      % else:
      <div>
      % endif
        <table class="vertical">
          <tr>
            <th>Username</th>
            % if c.mode == 'view':
            <td>${c.account.username}</td>
            % elif c.mode == 'edit':
            <td><input type="text" name="username" value="${c.account.username}"></td>
            % else:
            <td><input type="text" name="username"></td>
            % endif
          </tr>
          <tr>
            <th>Password</th>
            % if c.mode == 'view':
            <td><i>(hidden)</i><td>
            % else:
            <td><input type="password" name="password"></td>
            % endif
          </tr>
          <tr>
            <th>Filter tags</th>
            % if c.mode == 'view':
            <td>${c.account.required_tags}</td>
            % elif c.mode == 'edit':
            <td><input type="text" name="required_tags" value="${c.account.required_tags}"></td>
            % else:
            <td><input type="text" name="required_tags"></td>
            % endif
          </tr>
          % if c.mode == 'new':
          <tr>
            <th></th>
            <td class="submit"><input type="submit" value="Create"></td>
          </tr>
          % elif c.mode == 'edit':
          <tr>
            <th></th>
            <td class="submit"><a href="${h.url_for(action='view')}">Cancel</a> <input type="submit" value="Save"></td>
          </tr>
          % else:
          <tr>
            <th>Bookmarks</th>
            <td>${len(c.account.bookmarks)}</td>
          </tr>
          <tr>
            <th>Last updated</th>
            <td>${h.time_ago_in_words(c.account.last_updated, 'day')} ago</td>
          </tr>
          <tr>
            <th>Actions</th>
            <td>
              % if c.edit:
              <a href="${h.url_for(action='view', id=c.account.id)}">View</a>
              % else:
              <a href="${h.url_for(action='edit', id=c.account.id)}">Edit</a>
              % endif
              <form method="POST" action="${h.url_for(action='delete', id=c.account.id)}">
                <input type="submit" value="Delete">
              </form>
              <form method="POST" action="${h.url_for(action='update_bookmarks', id=c.account.id)}">
                <input type="submit" value="Check for updates">
              </form>
            </td>
          </tr>
          % endif
        </table>
      % if c.mode == 'view':
      </div>
      % else:
      </form>
      % endif
