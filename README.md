# AcmeAI Server

FastAPI backend server.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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
