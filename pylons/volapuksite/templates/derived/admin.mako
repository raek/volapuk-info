<%inherit file="/base/vp-base.mako" />
<%def name="breadcrumb()">
      <p>
        <b>Admin</b>
      </p>
</%def>
      <ul>
        <li><a href="${h.url_for(controller='/delicious_account')}">Delicious Accounts</a></li>
        <li><a href="${h.url_for(controller='/blog')}">Blogs</a></li>
        <li><a href="${h.url_for(controller='/twitter_hashtag')}">Twitter Hashtag</a></li>
      </ul>
