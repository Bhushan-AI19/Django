from flask import Flask
from flask_session import Session
import redis

app = Flask(__name__)

app.config.update(
    SESSION_TYPE = "redis",
    SESSION_REDIS = redis.Redis(host="localhost", port=6379),
    SESSION_PERMANENT = False
)

Session(app)

# Session data stored on server
# Cookie stores only session ID
# Scalable & secure
