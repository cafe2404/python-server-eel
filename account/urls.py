from rest_framework import routers
from account.views import UserViewSet, UserLoginViewSet, UserRegisterViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path(r'login', UserLoginViewSet.as_view(), name='login'),
    path(r'register', UserRegisterViewSet.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename='users')
urlpatterns += router.urls