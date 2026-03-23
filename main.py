from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

APP_DIR = Path(__file__).resolve().parent / "sql connect"
if str(APP_DIR) not in sys.path:
    # Ensure local imports like `import models` and `from db import ...` resolve.
    sys.path.insert(0, str(APP_DIR))

spec = spec_from_file_location("sql_connect_main", APP_DIR / "main.py")
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load app module from 'sql connect/main.py'")

module = module_from_spec(spec)
spec.loader.exec_module(module)
app = module.app