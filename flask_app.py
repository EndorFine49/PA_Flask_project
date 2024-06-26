# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="EndorFine",
    password="6RxLryxrPY#4yB",
    hostname="EndorFine.mysql.pythonanywhere-services.com",
    databasename="EndorFine$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__="comments"

    id=db.Column(db.Integer, primary_key = True)
    content=db.Column(db.String(4096))


sql_pass = '6RxLryxrPY#4yB'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html", comments=Comment.query.all())
    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/wibble')
def wibble():
    return 'This is something else'