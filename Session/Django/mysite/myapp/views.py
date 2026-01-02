from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome")

# Create Session (Login)
def login_view(request):
    request.session["user_id"] = 101
    request.session["username"]= "Bhushan"
    request.session.set_expiry(3600)
    return HttpResponse("Session Created. User logged in")


# Read Session
def dashboard_view(request):
    if request.session.get("user_id"):
        return HttpResponse(f"Welcome {request.session['username']}")
    return HttpResponse("Please login first!")


# Delete Session
def logout(request):
    request.session.flush()
    return HttpResponse("User logged out. Session cleared")