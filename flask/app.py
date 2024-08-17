from flask import Flask, jsonify, render_template, redirect, request, send_from_directory, session, url_for, g, session
from os import path, urandom
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, static_folder="./public/",static_url_path='/')
app.secret_key = urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



@app.route("/")
def mainpage():
    # load()
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)