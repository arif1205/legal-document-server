# AcmeAI Server

Legal documents mock API.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # For mac only
```

## Dependencies:

```bash
pip install -r requirements.txt
```

## Run:

```bash
python -m uvicorn main:app --reload --port 8000
```

## Endpoints

- `GET /health` - Health check endpoint
- `POST /generate` - Generate endpoint
