from rest_framework import routers
from account.views import UserViewSet, UserLoginViewSet, UserRegisterViewSet
from django.urls import path

urlpatterns = [
    path(r'login', UserLoginViewSet.as_view(), name='login'),
    path(r'register', UserRegisterViewSet.as_view(), name='register'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename='users')
urlpatterns += router.urls