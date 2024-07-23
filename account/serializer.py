from rest_framework import serializers
from account.models import Account

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
    