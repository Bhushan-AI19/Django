from flask import Flask

app = Flask(__name__)

app.secret_key = "super_secret_key"

app.config.update(
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SECURE = False, # Set True in production (HTTPS)
    SESSION_COOKIE_SAMESITE = "Lax",
    SESSION_COOKIE_LIFETIME = 3600
)

