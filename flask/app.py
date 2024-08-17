from flask import Flask, jsonify, render_template, redirect, request, session, url_for, g, session
from os import path, urandom
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/")
def mainpage():
    # load()
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)