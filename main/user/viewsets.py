from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.user.serializers import UserSerializer
from main.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'patch')
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
