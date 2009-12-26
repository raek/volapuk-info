<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <b>Volapük.info</b>
      </p>
</%def>
<%def name="sidebar()">
      <h2>Chat</h2>
      <p><a href="http://widget.mibbit.com/?settings=b7979beaded7832bccd41c7594386dee&amp;server=irc.unilang.org&amp;channel=%23volapuk&amp;noServerNotices=true&amp;noServerMotd=true&amp;autoConnect=true">Chat in you browser</a></p>
      <h2>News</h2>
      <ul>
        % for tag in c.tags:
        <li><a href="${h.url_for(action='by_tag', id=tag)}">${tag}</a></li>
        % endfor
      </ul>
</%def>
      <p>A big long text</p>
