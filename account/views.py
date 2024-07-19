from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,exceptions as rest_exxeptions
from account.models import Account
from account.serializer import UserSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

        
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    
class UserLoginViewSet(APIView):
    permission_classes = ()
    authentication_classes = ()
    def get(self,request):
        return Response({"message":"Method GET not allowed.","status":0},status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
            )
            if user:
                return Response({"message":"Đăng nhập thành công","status":1,"username":serializer.data['username']},status=status.HTTP_200_OK)
            else:
                raise rest_exxeptions.AuthenticationFailed("Tài khoản hoặc mật khẩu không đúng")
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserRegisterViewSet(APIView):
    permission_classes = ()
    authentication_classes = ()
    def get(self,request):
        return Response({"message":"Method GET not allowed.","status":0},status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            return Response({"message":"Đăng ký thành công","username":user.username,"status":1},status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)