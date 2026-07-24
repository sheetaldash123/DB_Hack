"""Deliberately INSECURE demo app — TENET's attack target.

DO NOT deploy. Contains planted vulnerabilities matching the sample SARIF so the
attacker/verifier agents have real code paths to exercise. The pipeline itself
is vuln-type agnostic; these are just seed examples.
"""
import hashlib
import os
import sqlite3

from flask import Flask, request

app = Flask(_name_)


def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT, role TEXT)")
    conn.execute("INSERT INTO users VALUES ('admin', 'admin'), ('bob', 'user')")
    return conn


@app.route("/login")
def login():
    name = request.args.get("name", "")
    # VULN: SQL injection (CWE-89)
    query = "SELECT * FROM users WHERE name='" + name + "'"
    rows = get_db().execute(query).fetchall()
    return {"authenticated": bool(rows), "rows": rows}


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # VULN: command injection (CWE-78)
    return os.popen("ping -c1 " + host).read()


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "0")
    # VULN: code injection (CWE-94)
    return {"result": eval(expr)}  # noqa: S307


@app.route("/hash")
def weak_hash():
    data = request.args.get("data", "")
    # VULN: weak crypto (CWE-327)
    return {"md5": hashlib.md5(data.encode()).hexdigest()}


if _name_ == "_main_":
    app.run(port=5055)"""Deliberately INSECURE demo app — TENET's attack target.

DO NOT deploy. Contains planted vulnerabilities matching the sample SARIF so the
attacker/verifier agents have real code paths to exercise. The pipeline itself
is vuln-type agnostic; these are just seed examples.
"""
import hashlib
import os
import sqlite3

from flask import Flask, request

app = Flask(_name_)


def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT, role TEXT)")
    conn.execute("INSERT INTO users VALUES ('admin', 'admin'), ('bob', 'user')")
    return conn


@app.route("/login")
def login():
    name = request.args.get("name", "")
    # VULN: SQL injection (CWE-89)
    query = "SELECT * FROM users WHERE name='" + name + "'"
    rows = get_db().execute(query).fetchall()
    return {"authenticated": bool(rows), "rows": rows}


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # VULN: command injection (CWE-78)
    return os.popen("ping -c1 " + host).read()


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "0")
    # VULN: code injection (CWE-94)
    return {"result": eval(expr)}  # noqa: S307


@app.route("/hash")
def weak_hash():
    data = request.args.get("data", "")
    # VULN: weak crypto (CWE-327)
    return {"md5": hashlib.md5(data.encode()).hexdigest()}


if _name_ == "_main_":
    app.run(port=5055)
