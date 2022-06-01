from django.urls import path,include
from . import views

urlpatterns = [
    path('register', views.register_request, name="register"),
    path('', include('main.urls')),
    path('login',views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout")
]