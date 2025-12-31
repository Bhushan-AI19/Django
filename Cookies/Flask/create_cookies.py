from flask import Flask, make_response

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