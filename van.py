# vulnerable_app.py
# WARNING: Intentionally vulnerable code for SAST testing only.

import os
import sqlite3
import subprocess
import hashlib
import pickle
from flask import Flask, request

app = Flask(__name__)

DATABASE = "users.db"


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Vulnerability: SQL Injection
    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "' AND password='"
        + password
        + "'"
    )

    cursor.execute(query)

    if cursor.fetchone():
        return "Login successful"

    return "Invalid credentials"


@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Vulnerability: Command Injection
    result = subprocess.check_output(
        "ping -c 1 " + host,
        shell=True
    )

    return result


@app.route("/read")
def read():
    filename = request.args.get("file")

    # Vulnerability: Path Traversal
    with open(filename, "r") as f:
        return f.read()


@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.data

    # Vulnerability: Unsafe Deserialization
    obj = pickle.loads(data)

    return str(obj)


@app.route("/hash")
def weak_hash():
    value = request.args.get("value")

    # Vulnerability: Weak Cryptographic Hash
    return hashlib.md5(value.encode()).hexdigest()


@app.route("/eval")
def evaluate():
    expression = request.args.get("expr")

    # Vulnerability: Arbitrary Code Execution
    return str(eval(expression))


@app.route("/exec")
def execute():
    code = request.args.get("code")

    # Vulnerability: Arbitrary Code Execution
    exec(code)

    return "Executed"


@app.route("/secret")
def secret():

    # Vulnerability: Hardcoded Secret
    api_key = "AKIA_TEST_SECRET_123456"

    return api_key


@app.route("/env")
def env():

    # Information Exposure
    return str(dict(os.environ))


if __name__ == "__main__":

    # Debug Mode Enabled
    app.run(debug=True)
