from django.urls import path
from .views import template_view, login_view, register_view, user_profile, logout_view, get_text

app_name = "app"

urlpatterns = [
    path("", login_view, name="home"),
    path("template/", template_view, name="template"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("profile/", user_profile, name="user_profile"),
    path("logout/", logout_view, name="logout"),
    path("get/text/", get_text, name="get_text"),
]