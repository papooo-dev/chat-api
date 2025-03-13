#!/bin/bash

# 가상환경 활성화
source .venv/bin/activate


# FastAPI 서버 실행
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
