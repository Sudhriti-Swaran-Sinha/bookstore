from django.urls import path
from . import views
urlpatterns = [

    path("", views.home_view, name="home"),
    path("login/", views.user_login_view, name="login"),
    path("sign/", views.sign_in_view, name="sign_in"),
    path("store/", views.store_view, name="store"),
    path('logout/', views.logout_view, name='logout'),
    
]
