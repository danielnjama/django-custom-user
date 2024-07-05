from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path("login/",views.login,name="login"),
    path("activate/",views.activate,name="activate"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout,name="logout"),
    path("resend/",views.send_activation_code,name="send_activation_code"),
]