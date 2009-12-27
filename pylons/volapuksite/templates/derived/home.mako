<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <b>Volapük.info</b>
      </p>
</%def>
<%def name="sidebar()">
      <h2>Chat</h2>
      <p>
        Join the <strong>#volapuk</strong> IRC channel on the
        <strong>irc.unilang.org</strong> network, or chat directly in your
        browser!
      </p>
      <p class="instructions">
        <a href="http://embed.mibbit.com/?server=irc.unilang.org&channel=%23volapuk">
          Click here to join the chat!
        </a>
      </p>
      <ul>
        % for tag in c.tags:
        <li><a href="${h.url_for(action='by_tag', id=tag)}">${tag}</a></li>
        % endfor
      </ul>
</%def>
      <p>A big long text</p>
