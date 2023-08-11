from datetime import datetime
import uuid

from django.db import models


class Personne(models.Model):
    personneID = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sexe = models.CharField(choices=[('M', 'masculin'), ('F', 'féminin')], max_length=1)
    date_naissance = models.DateField()
    pere = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='personnes_pere')
    mere = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='personnes_mere')


class Patient(Personne):
    patientID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_accueil = models.DateTimeField(auto_now=True)
    contact = models.CharField(max_length=9, null=True)


class Agent(Personne):
    agentID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricule = models.CharField(max_length=6, null=True)


class Imagerie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    categorie = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    technicien = models.ForeignKey(Agent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    date_image = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.id


class Resultats(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Imagerie, on_delete=models.CASCADE)
    interpreteur = models.ForeignKey(Agent, on_delete=models.CASCADE)
    result = models.TextField()
