from .models import Personne, Patient, Agent, Imagerie, Resultats
from rest_framework import serializers


class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class ImagerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagerie
        fields = '__all__'


class ResultatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultats
        fields = '__all__'
