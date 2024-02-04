from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signupuser/',views.signupuser,name='signupuser'),
    path('', views.home, name='home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),

]
