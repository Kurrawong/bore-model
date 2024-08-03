from pathlib import Path
from pylode.profiles.ontpub import OntPub

REPO_DIR = Path(__file__).parent.parent.resolve()

# initialise
od = OntPub(ontology=REPO_DIR / "bore.ttl")

# produce HTML
html = od.make_html()

# or save HTML to a file
od.make_html(destination=REPO_DIR / "bore.html")
