from rest_framework import viewsets, permissions,response,status
from task.models import Task
from task.serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Lấy queryset chỉ cho người dùng đã đăng nhập
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.none()
        
        
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.data['user'] = request.user.id
            return super().create(request, *args, **kwargs)
        else:
            return response.Response({'message': 'Bạn phải đăng nhập để tạo task'}, status=status.HTTP_401_UNAUTHORIZED)


