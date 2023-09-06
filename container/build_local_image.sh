#!/bin/bash
cp ../requirements.txt .
cp ../app.py .
docker build --build-arg host="127.0.0.1" -t clientxyz/py-api:latest .
rm app.py
rm requirements.txt