from rest_framework.routers import SimpleRouter

from .views import PersonneViewSet, AgentViewSet, PatientViewSet, ImagerieViewSet, ResultatViewSet

router = SimpleRouter()
router.register("personne", PersonneViewSet, basename="personne")
router.register("patient", PatientViewSet, basename="patient")
router.register("agent", AgentViewSet, basename="agent")
router.register("imagerie", ImagerieViewSet, basename="imagerie")
router.register("resultat", ResultatViewSet, basename="resultat")

urlpatterns = [
    *router.urls,
]
