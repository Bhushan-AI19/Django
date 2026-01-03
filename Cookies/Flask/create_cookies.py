from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set-cookie")
def set_cookie():
    response = make_response("Cookies has been set")
    response.set_cookie(
        key="username",
        value="bhushan",
        max_age=3600,   #sec
        httponly=True,  # Not accessible via JS
        secure=True,    # Only over HTTPS
        samesite="Lax"  # CSRF protection
    )

    return response

@app.route('/get-cookie')
def get_cookies():
    username = request.cookies.get("username")
    if username:
        return f"Hello {username}"
    return "No cookie found"

@app.route("/delete-cookie")
def delete_cookie():
    response = make_response("Cookie deleted")
    response.set_cookie("username", "", expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=False)