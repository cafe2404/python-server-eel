from rest_framework import routers, serializers, viewsets,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,exceptions as rest_exxeptions
from account.models import Account
from account.serializer import UserSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt import tokens
from django.conf import settings
from django.middleware import csrf

def get_token(user):
    refresh = tokens.RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    
    
    
class UserLoginViewSet(APIView):
    permission_classes = [permissions.AllowAny,]
    authentication_classes = ()
    def get(self,request):
        return Response({"message":"Method GET not allowed.","status":0},status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
            )
            if user:
                tokens = get_token(user)
                res = Response()
                res.set_cookie(
                    key =  settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value = tokens['access'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                )
                res.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                    value=tokens["refresh"],
                    expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                res.data = tokens
                res['X-CSRFToken'] = csrf.get_token(request)
                return res
            else:
                raise rest_exxeptions.AuthenticationFailed("Tài khoản hoặc mật khẩu không đúng")

        if serializer.errors.get("email"):
            detail = "Email không đng định dạng"
        elif serializer.errors.get("password"):
            detail = "Mật khẩu không được để trống"
        return Response({"detail":detail}, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserRegisterViewSet(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def get(self,request):
        return Response({"message":"Method GET not allowed.","status":0},status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            return Response({"message":"Đăng ký thành công","email":user.email,"status":1},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)