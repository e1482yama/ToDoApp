from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view()),
<<<<<<< HEAD
    path('detail', TodoDetail.as_view()),
=======
    path('detail/<int:pk>', TodoDetail.as_view()),
>>>>>>> abfeadd42205ac956cd97b544da3372668e89847
]
