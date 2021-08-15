from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'password', 'created', 'updated', 'deleted',]
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
    
    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = self.Meta.model.objects.create_user(email, password)
        return user