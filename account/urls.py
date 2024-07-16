from rest_framework import routers
from account.views import UserViewSet

urlpatterns = [
    
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns += router.urls