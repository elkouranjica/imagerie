from django.db import models


class Personne(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)
    date_naissance = models.DateField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'
