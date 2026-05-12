# GitHub Function Change Miner

Python research data collection pipeline that uses the GitHub REST API to:
- select 20 public Python repositories (created on or before 2023-12-31, non-archived, non-fork), ranked by stars
- find at least 5 Python files per repo where the **latest** pre-2024 adjacent commit pair contains an **existing function body change**
- write JSONL datasets with repository, file, and function-level change records

## Setup

1. Provide a GitHub token:

Option A: Put it in `.env`

```bash
# .env
GITHUB_TOKEN=...
```

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

Outputs are written to:
- `output/selected_repositories.jsonl`
- `output/changed_files.jsonl`
- `output/changed_functions.jsonl`

## Notes
- This project uses only the GitHub REST API (no HTML scraping).
- Filtering and selection settings live in `src/config.py` as constants (no CLI flags).
