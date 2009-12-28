<%def name="head()"/>
<%def name="breadcrumb()"/>
<%def name="sidebar()"/>
<!doctype html> 
<html>
  <head>
    <title>Volapük.info – ${c.title}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/styles/telid.css">
    <script type="text/javascript">
      var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
      document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
    </script>
    <script type="text/javascript">
      try {
        var pageTracker = _gat._getTracker("UA-9708673-3");
        pageTracker._trackPageview();
      } catch(err) {}
    </script>
    ${self.head()}
  </head>
  <body>
    <div id="header">
      <div class="logo">Volapük.info</div>
      <a class="nav_link" id="bal" href="${h.url_for(controller='/home')}">
        <div class="title">Home</div>
        <div class="desc">Introduction to the <br> Volapük language</div>
      </a>
      <a class="nav_link" id="tel" href="${h.url_for(controller='/learn')}">
        <div class="title">Learn</div>
        <div class="desc">Courses, grammars, <br> dictionaries, etc</div>
      </a>
      <a class="nav_link" id="kil" href="${h.url_for(controller='/read')}">
        <div class="title">Read</div>
        <div class="desc">Blogs in and about <br> Volapük</div>
      </a>
      <a class="nav_link" id="fol" href="${h.url_for(controller='/speak')}">
        <div class="title">Speak</div>
        <div class="desc">Where to get in <br> touch with Volapük</div>
      </a>
    </div>
    <div id="breadcrumb">
      ${self.breadcrumb()}
    </div>
    <div id="main">
      <div id="sidebar">
        ${self.sidebar()}
      </div>
      <div id="inner">
      <h1>${c.title}</h1>
      ${self.body()}
      </div>
    </div>
  </body>
</html>
  
