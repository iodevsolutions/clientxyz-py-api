# app.py
import time
import os
from flask import Flask, jsonify

# get the dynamic host name
host = os.environ.get('SSH_HOST', '127.0.0.1')

app = Flask(__name__)

description = """
                <!DOCTYPE html>
                <head>
                <title>REST API Landing Page</title>
                </head>
                <body>
                    <h3>A very very simple REST API using that returns a JSON \
                    payload with the current timestamp</h3>
                    <a href="http://{host}:7080/api">http://{host}:7080/api</a>
                </body>
                """.format(host=host)


# Routes refer to url'
# our root url '/' will show our html description
@app.get("/")
def get_description():
    # return a html format string that is rendered in the browser
    return description


@app.get("/api")
def get_automate():
    ts = round(time.time())
    automate = {'message': 'Automate all the things!', 'timestamp': ts}
    return jsonify(automate)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7080)
