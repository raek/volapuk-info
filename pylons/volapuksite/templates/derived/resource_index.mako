<%inherit file="/base/resources.mako" />
<%def name="breadcrumb()">
      <p>
        <a href="${h.url_for('/')}">Volapük.info</a>
        → <b>Learn</b>
      </p>
</%def>
      <p>
        When learning and using a language, three kinds of resources are
        important:
      </p>
      <ol>
        <li><a href="${h.url_for(action='category', id='course')}">course material</a>
          that teaches the language
        </li>
        <li><a href="${h.url_for(action='category', id='dictionary')}">dictionaries</a>
          to look up words
        </li>
        <li><a href="${h.url_for(action='category', id='grammar')}">grammars</a>
          to look up grammatical words, constructs and rules.
        </li>
      </ol>
      <p>
        As for course material, there are two excellent choices:
        <a href="http://personal.southern.edu/~caviness/Volapuk/VolVifik/volvif00.html">Volapük Vifik</a>
        for de Jong's revised Volapük and
        <a href="http://personal.southern.edu/~caviness/Volapuk/HBoV/">Handbook of Volapük</a>
        for Schleyer's original version.
        <!--The more linguistically experienced might alternatively be
        interested in reading a grammar.-->
      </p>
      <p>
        Gramars often comes in either a detailed explaining form or a brief
        summarizing form. Great works include
        <a href="http://www.freewebs.com/volapoke/">Volapoke</a>,
        a detailed reference grammar and
        <a href="http://www.panix.com/~bartlett/volgram.html">Volapük Grammatical Forms</a>,
        a summary on prefixes, suffixes and function words.
      </p>
