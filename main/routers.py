from rest_framework import routers

from main.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from main.user.viewsets import UserViewSet
from main.personne.viewsets import PersonneViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'personne/', PersonneViewSet, basename='personne')

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
   *router.urls,
]
