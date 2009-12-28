<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for('/')}">Volapük.info</a>
        → <b>Home</b>
      </p>
</%def>
<%def name="sidebar()">
      <h2>Chat</h2>
      <p>
        Join the <strong>#volapuk</strong> IRC channel on the
        <strong>irc.unilang.org</strong> network, or chat directly in your
        browser!
      </p>
      <p>
        <a class="instructions"
            href="http://embed.mibbit.com/?server=irc.unilang.org&channel=%23volapuk">
          Click here to join the chat!
        </a>
      </p>
      <ul>
        % for tag in c.tags:
        <li><a href="${h.url_for(action='by_tag', id=tag)}">${tag}</a></li>
        % endfor
      </ul>
</%def>
      <p>
        Volapük is a constructed international language created in 1879–1880
        by Johann Martin Schleyer, a Roman Catholic priest in Baden, Germany.
        It was the first international auxiliary language that was widely
        used.
      </p>
      <p>
        This website is intended to be a resource for helping people learn
        and use Volapük, and to introduce them to the Volapük speaking
        community.
      </p>
