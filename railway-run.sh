#!/bin/bash

playwright install
uvicorn news_today:app --host=0.0.0.0 --port=8000
