from rest_framework import viewsets
from basic_django_app.views import SafeDeleteViewSet
from users.models import User
from users.api.serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(SafeDeleteViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer