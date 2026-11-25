"""Copy the bundled entry image to the output directory deterministically, without network access or randomness."""

import os
import shutil
from pathlib import Path

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.png"
shutil.copyfile(Path(__file__).with_name("entry.png"), output_file)
# Ignore chmod failures because the grader runs unprivileged on a read-only filesystem.
try:
    output_file.chmod(0o644)
except OSError:
    pass
