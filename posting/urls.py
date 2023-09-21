from django.urls import path

from posting import views
app_name= 'posting'

urlpatterns = [
    path('',views.getTaskList,name='getTaskList'),
    path('addTask',views.addTask,name='addTask'),
    path('updateTask/<int:pk>/<str:work>',views.updateTask,name='updateTask'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask')
]