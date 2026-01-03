from flask import make_response, Flask

app = Flask(__name__)

@app.route("/delete-cookie")
def delete_cookie():
    response = make_response("Cookie deleted")
    response.set_cookie("username", "", expires=0)
    return response