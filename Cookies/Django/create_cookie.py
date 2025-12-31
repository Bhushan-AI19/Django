from django.http import HttpResponse

def set_cookie():
    response = HttpResponse("Cookies has been sent")
    response.set_cookie(
        key="username",
        value="bhushan",
        max_age=3600,   #sec
        httponly=True,  # Prevent JS access
        secure=True,    # HTTPS only
        samesite="Lax"  # CSRF protection
    )

    return response