from main.personne.models import Personne
from rest_framework import serializers


class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'
