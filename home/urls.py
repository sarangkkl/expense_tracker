from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="home"),
    path("add_category",views.add_category,name="add_category"),
    path("login",views.login_handle,name="login"),
    path("logout",views.logout_handle,name="logout"),
    path("register",views.handle_register,name="register"),
]
