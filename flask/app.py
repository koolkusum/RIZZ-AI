from flask import Flask, jsonify, render_template, redirect, request, session, url_for, g, session

app = Flask(__name__)
app.secret_key = urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

if __name__ == "__main__":
    app.run(debug=True)