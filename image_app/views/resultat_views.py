from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from image_app.models import Resultats, Agent, Imagerie
from image_app.serializers import ResultatSerializer

from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAdminUser])
def allResultats(request):
    try:
        resultat = resultat.objects.all()
        serialisation = ResultatSerializer(resultat, many=True)
        res = serialisation.data
    except: 
        res = {'status': 'warning', 'message': 'Une erreur c\'est produite, essayez plus tard'}
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getResultatById(request, pk):
    try:
        resultat = resultat.objects.get(id=id)
        serialisation = PatientSerializer([resultat], many=False)
        res = serialisation.data
    except ValidationError:
        res = {'status': 'error', 'message': 'Identifiant Invalide'}
    except:
        res = {'status': 'warning', 'message': 'Donnee introuvable'}
    return Response(res)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def addResultat(request):
    try:
        serialisation = ResultatSerializer(data=request.data, many=False)
        res = None;
        if serialisation.is_valid():
            serialisation.save()
            res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'une resultat effectuée' }
        else:
            res = {'status': 'warning', 'message': "Entreés invalides"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res);


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateResultat(request, pk):
    try:
        resultat = Resultat.objects.get(id=id);
        resultat.Imagerie.id = request.data['categorie']
        resultat.Agent.id = request.data['interperteur']
        resultat.result = request.data['result']
        resultat.save()
        res = {'status': 'success', "message": "Mis à jour des infos réussi"}
    except ValidationError:
        res = {'status': 'error', 'message': "Patient introuvable introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteResultat(request, id):
    try:
        Resultat = Resultat.objects.get(id=id)
        Resultat.delete()
        res = {'status': 'success', 'message': 'Suppression d\'une Resultat réussi'}
    except ValidationError:
        res = {'status': 'warning', 'message': "Agent introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)
