# Fetch Rewards – Receipt Processor API

## Overview
A high‑performance FastAPI service that awards points to receipts per the rules
defined in the Fetch backend challenge.  
Designed with **clean architecture**, **OOP/SOLID** principles, and full
typing for maintainability and speed.

## Quick Start

```bash
# Build & run with Docker
docker build -t receipt-api .
docker run -p 8000:8000 receipt-api
```

Visit `http://localhost:8000/docs` for interactive Swagger UI.

## Project Structure
```
app/
├── api/          # REST endpoints
├── core/         # Scoring rules & processor (domain logic)
├── models/       # Pydantic schemas & dataclass entities
└── services/     # In‑memory store abstraction
tests/            # Pytest unit tests
```

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
