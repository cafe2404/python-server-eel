from rest_framework import routers
from task.views import TaskViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet,basename='tasks')
urlpatterns = [
    path('', include(router.urls)),
]