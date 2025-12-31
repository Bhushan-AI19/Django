from django.http import HttpResponse

def get_cookie(request):
    username = request.COOKIES.get("username")
    if username:
        return HttpResponse(f"Hello {username}")
    return HttpResponse("No cookie found")