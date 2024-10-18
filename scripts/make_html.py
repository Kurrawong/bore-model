from pathlib import Path
from pylode.profiles.ontpub import OntPub
import re
from textwrap import indent

REPO_DIR = Path(__file__).parent.parent.resolve()

# initialise
od = OntPub(ontology=REPO_DIR / "model.ttl")

# make HTML
html = od.make_html()

# post-process HTML to put in images
# deduplicate id="bore"
before = '''<dl>
          <dt id="bore">bore</dt>'''
after = '''<dl>
          <dt id="b">bore</dt>'''
html = html.replace(before, after)

# add overview figure
name = re.findall(r"<h1>(.*)</h1>", html)[0]
name_plus_img = f'''<h1>{name}</h1>
      {open(REPO_DIR / "img" / "Concepts.svg").read()}
      <br /><br />
      <img src="img/Overview.png" style="width:600px;" />
      '''
html = indent(re.sub(r"<h1>(.*)</h1>", name_plus_img, html), "        ")

# concepts_img = f'''<div id="content">
#       <h1>Bore Model</h1>
#       {open(REPO_DIR / "img" / "Concepts.svg").read()}
#       <br /><br />
#       <img src="img/Overview.png" style="width:600px;" />
# '''
# html = html.replace('<div id="content">', concepts_img)

# write HTML to file
open(REPO_DIR / "model.html", "w").write(html)
