"""news-image-20261123 entry (Python 3.13, standard library only).

The repository holds the day's front page as entry.png beside this file;
the program copies it to the output directory as entry.png, verifying
the image signature before the copy and the written bytes afterwards.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"

ASSET_NAME = "entry.png"


def asset_path() -> Path:
    """The bundled front page, resolved relative to this file."""
    return Path(__file__).resolve().parent / ASSET_NAME


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / ASSET_NAME


def check_signature(data: bytes) -> None:
    """Raise ValueError unless the bytes start as a PNG or a JPEG."""
    if data.startswith(PNG_SIGNATURE) or data.startswith(JPEG_SIGNATURE):
        return
    raise ValueError("bundled asset is neither a PNG nor a JPEG image")


def load_asset() -> bytes:
    """Read the bundled front page and verify its image signature."""
    data = asset_path().read_bytes()
    check_signature(data)
    return data


def write_entry(data: bytes) -> Path:
    """Write the entry image, then read it back and verify it in full."""
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    written = target.read_bytes()
    if len(written) != len(data):
        raise IOError(
            f"read-back length {len(written)} != asset length {len(data)}"
        )
    check_signature(written)
    return target


def main() -> None:
    target = write_entry(load_asset())
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
