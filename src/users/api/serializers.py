from rest_framework import serializers
from basic_django_app.serializers import EntitySerializer
from django.contrib.auth.hashers import make_password

from users.models import User


class UserSerializer(EntitySerializer):
    class Meta(EntitySerializer.Meta):
        model = User
        fields = EntitySerializer.Meta.fields + [
            'email', 
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)