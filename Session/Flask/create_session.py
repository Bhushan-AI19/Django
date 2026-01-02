from flask import Flask
from flask import session

app = Flask(__name__)
app.config["SECRET-KEY"] = "super-secret-key"

@app.route("/login")
def login():
    session["user_id"] = "101"
    session["username"] = "bhushan"
    return "User logged in."