# Server-side session using Redis (recommended for real apps)

from flask import Flask, session
from flask_session import Session
import redis

app = Flask(__name__)
app.secret_key = "super-secret-key"

# Redis session configuration
app.config.update(
    SESSION_TYPE = "redis",
    SESSION_REDIS = redis.Redis(host="localhost", port=6379),
    SESSION_PERMANENT = False,
    SESSION_USE_SIGNER = True,
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SECURE = False, # True in production
    SESSION_COOKIE_SAMESITE = "Lax"
    )

Session(app)

@app.route("/")
def home():
    return "Welcome"


# LOGIN – CREATE SESSION
@app.route("/login")
def login():
    session["user_id"] = 101
    session["username"] = "Bhushan"
    return f"User logged in (server-side session)"


# READ SESSION
@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return f"Welcome {session['username']}"
    return "Please Log in"


# LOGOUT - SESSION CLEARED
@app.route("/logout")
def logout():
    session.clear()
    return "Logged Out, Session Cleared"


if __name__ == "__main__":
    app.run(debug=True)