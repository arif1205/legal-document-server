# AcmeAI Server

Legal documents mock API.

## Dependencies:

- Python 3.10
- FastAPI==0.104.1
- Uvicorn[standard]==0.24.0
- Pydantic==2.5.0

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
