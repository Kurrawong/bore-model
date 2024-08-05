from pathlib import Path
from pylode.profiles.ontpub import OntPub

REPO_DIR = Path(__file__).parent.parent.resolve()

# initialise
od = OntPub(ontology=REPO_DIR / "bore.ttl")

# make HTML
html = od.make_html()

# post-process HTML to put in images
# deduplicate id="bore"
before = '''<dl>
          <dt id="bore">bore</dt>'''
after = '''<dl>
          <dt id="b">bore</dt>'''
html = html.replace(before, after)

# remove title
html = html.replace('<h1>Bore Model</h1>\n',  '')

# add overview figure
concepts_img = f'''<div id="content">
      <h1>Bore Model</h1>
      {open(REPO_DIR / "img" / "Concepts.svg").read()}
      <br /><br />
      <img src="img/Overview.png" style="width:600px;" /> 
'''
html = html.replace('<div id="content">', concepts_img)

# write HTML to file
open(REPO_DIR / "bore.html", "w").write(html)
