from django.contrib import admin
from django.urls.conf import include, path
from rest_framework import routers

from users.api.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls