from django.http import HttpResponse

def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie("username")
    return response