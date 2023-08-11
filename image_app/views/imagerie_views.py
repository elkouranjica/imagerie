from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from image_app.models import Agent, Patient, Imagerie
from image_app.serializers import ImagerieSerializer

from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAdminUser])
def allImageries(request):
    try:
        imagerie = imagerie.objects.all()
        serialisation = ImagerieSerializer(imagerie, many=True)
        res = serialisation.data
    except: 
        res = {'status': 'warning', 'message': 'Une erreur c\'est produite, essayez plus tard'}
    return Response(res)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getImagerieById(request, pk):
    try:
        imagerie = imagerie.objects.get(id=id)
        serialisation = PatientSerializer([imagerie], many=False)
        res = serialisation.data
    except ValidationError:
        res = {'status': 'error', 'message': 'Identifiant Invalide'}
    except:
        res = {'status': 'warning', 'message': 'Donnee introuvable'}
    return Response(res)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def addImagerie(request):
    try:
        serialisation = ImagerieSerializer(data=request.data, many=False)
        res = None;
        if serialisation.is_valid():
            serialisation.save()
            res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'une imagerie effectuée' }
        else:
            res = {'status': 'warning', 'message': "Entreés invalides"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res);


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateImagerie(request, pk):
    try:
        imagerie = Patient.objects.get(id=id);
        imagerie.categorie = request.data['categorie']
        imagerie.Patient.patientID = request.data['patient']
        imagerie.Agent.agentID= request.data['technicien']
        imagerie.image = uploadImage(request)
        imagerie.save()
        res = {'status': 'success', "message": "Mis à jour des infos réussi"}
    except ValidationError:
        res = {'status': 'error', 'message': "Patient introuvable introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteImagerie(request, id):
    try:
        Imagerie = Imagerie.objects.get(id=id)
        Imagerie.delete()
        res = {'status': 'success', 'message': 'Suppression d\'une Imagerie réussi'}
    except ValidationError:
        res = {'status': 'warning', 'message': "Agent introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data
    imagerie_id = data['id']
    imagerie = Imagerie.objects.get(id=id)
    imagerie.image = request.FILES.get('image')
    imagerie.save()

    return Response('Image was uploaded')

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getuuid(request):
    uuid = uuid.uuid1()
    res = {'uuid': uuid}
    return Response(res)