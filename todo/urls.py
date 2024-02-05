from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    path('createtodo/',views.createtodo,name='createtodo'),

]