
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/wibble')
def wibble():
    return 'This is something else'

