from flask import Flask, render_template, request
from caesar import cipher

# set up app
app = Flask(__name__, static_folder="static", static_url_path="")
SHIFT = 3

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/encrypt")
def encrypt():
    message = request.args.get("message")
    if message:
        return cipher(message, -SHIFT)
    return ""

@app.route("/decrypt")
def decrypt():
    message = request.args.get("message")
    if message:
        return cipher(message, SHIFT)
    return ""
