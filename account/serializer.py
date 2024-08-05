from rest_framework import serializers
from account.models import Account
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt import exceptions as rest_exceptions

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id','profile_picture', 'username', 'email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    

class CookieTokenRefreshSerializer(jwt_serializers.TokenRefreshSerializer):
    refresh = None
    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise rest_exceptions.InvalidToken(
                'No valid token found in cookie \'refresh\'')
