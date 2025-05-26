# Fetch Rewards – Receipt Processor API

## Overview
A high-performance **FastAPI** service that awards points to receipts according to the rules in the Fetch backend challenge.  
Built with **clean architecture**, **OOP / SOLID** principles, and full typing for maintainability and speed.

---

## Quick Start

```bash
# Build & run with Docker
docker build -t receipt-api .
docker run -p 8000:8000 receipt-api
```

## Quick Health Check
Once the container is running, verify the API with a single cURL:

```bash
curl http://localhost:8000/
# ➜ {"message":"Receipt-Processor API up and running. Visit /docs for Swagger UI."}
```

If you see that JSON response, the service is healthy.
Open <http://localhost:8000/docs> for the full interactive Swagger UI.


## Project Structure

```
app/
├── api/          # REST endpoints
├── core/         # Scoring rules & processor (domain logic)
├── models/       # Pydantic schemas & dataclass entities
└── services/     # In-memory store abstraction
scripts/         # smoke.sh (e2e)
tests/            # Pytest unit tests
```

## Local Dev (without Docker)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Now browse to localhost:8000/docs.

## Running Tests

```bash
pip install -r requirements.txt
pytest
```

## Design Highlights
- **FastAPI** & **Uvicorn** async server for >30k req/s on modest hardware.
- **Immutability & `slots`** in entities for memory savings & speed.
- **Rule objects** encapsulate individual scoring logic (SRP).
- **ReceiptProcessor** aggregates rules, enabling easy extension/testing.
- **In‑memory store** isolate persistence layer behind `ReceiptStore`.
- **Fully typed** (PEP‑604) and lint‑ready (flake8, isort recommended).

File scripts/smoke.sh does end-to-end test against Docker.