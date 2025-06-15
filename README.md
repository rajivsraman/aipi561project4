# AIPI 561 (Operationalizing AI) - Week 5 Project
### Author: Rajiv Raman
### Institution: Duke University
### Date: June 15th, 2025

## Overview

A production-style text generation REST API using Amazon Bedrock. This service supports content filtering and usage tracking in addition to generation.

## Features

- POST `/generate` endpoint for text completion
- Inference using Titan or Claude via Bedrock
- Prompt content filtering for blocked terms
- Usage logging to JSONL (`usage_log.jsonl`)
- Unit tests with mocked inference responses
- Test coverage via `pytest-cov`

## File Overview

- `main.py` – API endpoint logic
- `bedrock_client.py` – Model invocation using boto3
- `filter.py` – Blacklist-based prompt validation
- `monitor.py` – Logs request metadata and model usage
- `tests/test_api.py` – Unit tests using FastAPI TestClient

## Requirements

- boto3
- fastapi
- uvicorn
- pytest
- httpx

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

API documentation is available at:

```
http://127.0.0.1:8000/docs
```

## Running Tests

```bash
pytest --cov=.
```

## Notes

- AWS credentials must be configured via `aws configure`
- Model ID must match a model available in your Bedrock account
