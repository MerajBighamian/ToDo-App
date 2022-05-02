from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index , name= 'index'), # define index route
    path('update_task/<int:pk>', views.updateTask, name='update_task'), # define update task route
    path('delete_task/<int:pk>', views.deleteTask, name='delete_task'), # define delete task route
]