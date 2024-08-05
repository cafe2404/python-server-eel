from rest_framework import routers
from account import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path(r'login', views.UserLoginViewSet.as_view(), name='login'),
    path(r'register', views.UserRegisterViewSet.as_view(), name='register'),
    path('refresh-token', views.CookieTokenRefreshView.as_view(),name='refresh'),
    path('users/me', views.CurrentUserViewSet.as_view(), name='current-user'),
    path('logout', views.LogoutViewSet.as_view(), name='logout'),
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet,basename='users')
urlpatterns += router.urls