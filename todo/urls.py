from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    path('createtodo/',views.createtodo,name='createtodo'),
    path('currenttodo/', views.currenttodo, name='currenttodo'),
    path('updatetodo/<int:todo_id>', views.updatetodo, name='updatetodo'),
    path('deletetodo/<int:todo_id>', views.deletetodo, name='deletetodo'),

]