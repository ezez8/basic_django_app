from rest_framework import routers

from movies.api.views import ParticipationViewSet, FilmViewSet, ActorViewSet


router = routers.DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'participations', ParticipationViewSet)

urlpatterns = router.urls