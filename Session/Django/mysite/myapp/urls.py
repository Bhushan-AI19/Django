from django.urls import path
from .views import login_view, dashboard_view, logout, home

urlpatterns = [
    path("", home),
    path("login/", login_view),
    path("dashboard/", dashboard_view),
    path("logout/", logout)
]