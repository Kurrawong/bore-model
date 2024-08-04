import sys
from pathlib import Path
import tomllib
from datetime import datetime

REPO_DIR = Path(__file__).parent.parent.resolve()

with open("pyproject.toml", "rb") as f:
    pyproj = tomllib.load(f)

mkdn = f'''# {pyproj["tool"]["poetry"]["name"]}

### v{pyproj["tool"]["poetry"]["version"]}

{pyproj["tool"]["poetry"]["description"]}

Online at: <{pyproj["tool"]["poetry"]["repository"]}>

## Contacts

* {"* ".join([x + "  \n" for x in pyproj["tool"]["poetry"]["authors"]])}

## License & Rights

{pyproj["tool"]["poetry"]["license"]}

&copy; KurrawongAI, {datetime.now().strftime("%Y")}
'''

open(REPO_DIR / "README.md", "w").write(mkdn)
