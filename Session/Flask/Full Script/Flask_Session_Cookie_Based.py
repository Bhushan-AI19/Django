from flask import Flask, session

app = Flask(__name__)

# Required for session signing
app.secret_key = "secret_key"

# Session security configuration
app.config.update(
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SECURE = False, # Set True in production (HTTPS)
    SESSION_COOKIE_SAMESITE = "Lax",
    SESSION_COOKIE_LIFETIME = 3600
)

@app.route("/")
def home():
    return "Home Page"

# LOGIN – CREATE SESSION
@app.route("/login")
def login():
    session["user_id"] = 101
    session["username"] = "bhushan"
    session.permanent = True
    return "User logged in, Session created."


# READ SESSION
@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return f"Welcome {session["username"]}"
    return "Please Login"


# LOGOUT – DELETE SESSION
@app.route("/logout")
def logout():
    session.clear()
    return "User logged out, Session cleared."


if __name__ == "__main__":
    app.run(debug=True)