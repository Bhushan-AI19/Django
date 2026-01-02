from flask import Flask
from flask import session

app = Flask(__name__)
app.config["SECRET-KEY"] = "super-secret-key"

@app.route("/logout")
def logout():
    session.clear()
    return "User logged out, Session cleared."