from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.loginPage,name='loginpage'),
    path("login/",views.UserReg,name="login"),
    path("register/",views.signpage,name='register'),
    path("registeruser/",views.signup,name='regus'),
]