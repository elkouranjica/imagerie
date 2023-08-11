from rest_framework import viewsets
from main.personne.models import Personne
from main.personne.serializers import PersonneSerializer


class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
