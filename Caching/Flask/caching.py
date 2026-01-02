from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

# Cache configuration (Redis)
app.config.update(
    CACHE_TYPE = "RedisCache",
    CACHE_REDIS_HOST = "localhost",
    CACHE_REDIS_PORT = 6379,
    CACHE_DEFAULT_TIMEOUT = 60
)

cache = Cache()

# Attach cache to Flask app
cache.init_app(app)

@app.route("/")
def home():
    return "Flask Cache Example"


# CACHE API RESPONSE
@app.route("/slow-api")
@cache.cached(timeout=30)
def slow_api():
    time.sleep(5) # Simulate slow DB or API call
    return jsonify({'message':'Cached Response', 'time':time.time()})


# CACHE WITH KEY PREFIX
@app.route("/user/<int:user_id>")
@cache.cached(timeout=60, key_prefix="user_profile")
def user_profile(user_id):
    time.sleep(3)
    return jsonify({'user_id':user_id, 'name':'Bhushan'})


# MANUAL CACHE SET/GET
@app.route('/manual-cache')
def manual_cache():
    data = cache.get("stats")
    if not data:
        data = {"visits": 100}
        cache.set("stats", data, timeout=120)
    return jsonify(data)


# CLEAR CACHE
@app.route("/clear-cache")
def clear_cache():
    cache.clear()
    return "Cache cleared"


if __name__ == "__main__":
    app.run(debug=True)