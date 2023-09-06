FROM python:slim

WORKDIR /usr/src/app

# set dynamic host used on landing page
ARG host
ENV SSH_HOST $host

# copy all files first 
COPY requirements.txt app.py startweb.sh ./

# pip install all requirments
RUN pip install --no-cache-dir -r requirements.txt

# export port for gunicorn
EXPOSE 8000

# run bash script to start gunicorn as ENTRYPOINT
ENTRYPOINT ["./startweb.sh"]

