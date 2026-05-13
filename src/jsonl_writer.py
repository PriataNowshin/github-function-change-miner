from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def save_data_as_jsonl(path: str | Path, rows: List[Dict[str, Any]]) -> None:
    """Write an iterable of records to a JSON Lines (JSONL) file.

    Writes one JSON object per line and overwrites any existing file at `path`.
    If `path` includes a parent directory, it is created automatically.

    Args:
        path: Output file path (e.g., "output/function_changes.jsonl").
        rows: List of JSON-serializable mapping objects.
    """
    p = Path(path)
    if p.parent != Path("."):
        p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False))
            f.write("\n")
