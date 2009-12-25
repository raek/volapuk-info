<%def name="head()"/>
<%def name="breadcrumb()"/>
<!doctype html> 
<html>
  <head>
    <title>Volapük.info – ${c.title}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/styles/telid.css">
    ${self.head()}
  </head>
  <body>
    <div id="header">
      <div class="logo">Volapük.info</div>
      <a class="nav_link" id="bal" href="/front">
        <div class="title">Home</div>
        <div class="desc">Introduction to the <br> Volapük language</div>
      </a>
      <a class="nav_link" id="tel" href="/learn">
        <div class="title">Learn</div>
        <div class="desc">Courses, grammars, <br> dictionaries, etc</div>
      </a>
      <a class="nav_link" id="kil" href="/blogs">
        <div class="title">Read</div>
        <div class="desc">Blogs in and about <br> Volapük</div>
      </a>
      <a class="nav_link" id="fol" href="/social">
        <div class="title">Speak</div>
        <div class="desc">Where to get in <br> touch with Volapük</div>
      </a>
    </div>
    <div id="breadcrumb">
      ${self.breadcrumb()}
    </div>
    <div id="main">
      <h1>${c.title}</h1>
      ${self.body()}
    </div>
    <div id="footer">&nbsp;
    </div>
  </body>
</html>
  
