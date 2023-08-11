from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from image_app.serializers import PersonneSerializer
from image_app.models import Personne
from django.core.exceptions import ValidationError

# GET PERSONNE 
@api_view(['GET'])
@permission_classes([IsAdminUser])
def allPersonnes(request):
    try:
        personne = Personne.objects.all()
        serialisation = PersonneSerializer(personne, many=True)
        res = serialisation.data
    except: 
        res = {'status': 'warning', 'message': 'Une erreur c\'est produite, essayez plus tard'}
    return Response(res)

# GET PERSONNE  BY ID
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getpersonneById(request, id):
    try:
        personne = Personne.objects.get(personneID=id)
        serialisation = PersonneSerializer(personne, many=False)
        res = serialisation.data
    except ValidationError:
        res = {'status': 'error', 'message': 'Identifiant Invalide'}
    except:
        res = {'status': 'warning', 'message': 'Donnee introuvable'}
    return Response(res)

# ADD NEW ANNEE UNIV
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addPersonne(request):
    try:
        serialisation = PersonneSerializer(data=request.data, many=False)
        res = None;
        if serialisation.is_valid():
            serialisation.save()
            res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'une personne effectuée' }
        else:
            res = {'status': 'warning', 'message': "Entreés invalides"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res);


# UPDATE PERSONNE
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePersonne(request, id):
    try:
        personne = Personne.objects.get(personne=id);
        personne.nom = request.data['nom']
        personne.prenom = request.data['prenom']
        personne.sexe = request.data['sexe']
        personne.pere = request.data['pere']
        personne.mere = request.data['mere']
        personne.save()
        res = {'status': 'success', "message": "Mis à jour des infos réussi"}
    except ValidationError:
        res = {'status': 'error', 'message': "Personne introuvable introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)

# DELETE PERSONNE
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePersonne(request, id):
    try:
        Personne = Personne.objects.get(personneID=id)
        Personne.delete()
        res = {'status': 'success', 'message': 'Suppression d\'un Personne réussi'}
    except ValidationError:
        res = {'status': 'warning', 'message': "Personne introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)