"""Copy the entry picture that was picked here into the output directory.

The picture is chosen right here: it is the ``entry.jpg`` sitting beside this
script, and it is copied over byte for byte, never rebuilt. The output
directory is ``$MAKEFUN_OUTPUT_DIR`` when that variable is set, otherwise
``/output``; the copy lands there under the name ``entry.png``.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.jpg"
TARGET_NAME = "entry.png"


def output_dir() -> Path:
    """Return the directory the entry image is written to."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    # Re-encoding is off the table: a decode/encode round trip would nudge
    # pixels and colour, so the output would stop being the chosen picture.
    # Copied, not re-encoded: the JPEG bytes are the entry, and decoding and
    # re-encoding them would change the picture and make runs non-identical.
    shutil.copyfile(SOURCE, destination / TARGET_NAME)


if __name__ == "__main__":
    main()
