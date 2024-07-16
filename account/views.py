from rest_framework import routers, serializers, viewsets
from account.models import Account

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id','profile_picture', 'username', 'email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    

