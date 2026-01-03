from flask import request, Flask

app = Flask(__name__)

@app.route('/get-cookie')
def get_cookies():
    username = request.cookies.get("username")
    if username:
        return f"Hello {username}"
    return "No cookie found"