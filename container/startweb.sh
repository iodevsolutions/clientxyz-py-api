#!/bin/bash
# run gunicorn with two workers (CPU*2) and default local flask app
exec gunicorn -w 2 -b 0.0.0.0:8000 'app:app'
