from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from main.personne.models import Personne


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, matricule, password=None):
        if matricule is None:
            raise TypeError('Le numéro de matricule est obligatoire.')
        if password is None:
            raise TypeError('Vous devez saisir un mot de passe.')
        user = self.model(matricule=matricule)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricule, password=None):
        user = self.create_user(matricule, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    matricule = models.CharField(db_index=True, max_length=6, unique=True)
    personne = models.OneToOneField(Personne, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'matricule'

    def __str__(self):
        return self.matricule

    @property
    def is_staff(self):
        return self.is_superuser
