from flask import Flask
from flask import session

app = Flask(__name__)
app.config["SECRET-KEY"] = "super-secret-key"

@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return f"Welcome {session["username"]}"
    return "Please Login"