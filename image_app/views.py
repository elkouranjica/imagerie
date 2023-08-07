from rest_framework import viewsets
from .serializers import PersonneSerializer, PatientSerializer, AgentSerializer,\
    ImagerieSerializer, ResultatSerializer
from .models import Personne, Patient, Agent, Imagerie, Resultats


class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ImagerieViewSet(viewsets.ModelViewSet):
    queryset = Imagerie.objects.all()
    serializer_class = ImagerieSerializer


class ResultatViewSet(viewsets.ModelViewSet):
    queryset = Resultats.objects.all()
    serializer_class = ResultatSerializer
