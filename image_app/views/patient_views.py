from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from image_app.serializers import PatientSerializer
from image_app.models import Patient
from django.core.exceptions import ValidationError

# GET PATIENT
@api_view(['GET'])
@permission_classes([IsAdminUser])
def allPatients(request):
    try:
        patient = Patient.objects.all()
        serialisation = PatientSerializer(patient, many=True)
        res = serialisation.data
    except: 
        res = {'status': 'warning', 'message': 'Une erreur c\'est produite, essayez plus tard'}
    return Response(res)

# GET PATIENT  BY ID
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getPatientById(request, id):
    try:
        patient = Patient.objects.get(patientID=id)
        serialisation = PatientSerializer([patient], many=False)
        res = serialisation.data
    except ValidationError:
        res = {'status': 'error', 'message': 'Identifiant Invalide'}
    except:
        res = {'status': 'warning', 'message': 'Donnee introuvable'}
    return Response(res)

# ADD NEW PATIENT
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addPatient(request):
    try:
        serialisation = PatientSerializer(data=request.data, many=False)
        res = None;
        if serialisation.is_valid():
            serialisation.save()
            res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'une patient effectuée' }
        else:
            res = {'status': 'warning', 'message': "Entreés invalides"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res);


# UPDATE PATIENT
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePatient(request, id):
    try:
        patient = Patient.objects.get(patientID=id);
        patient.date_accueil = request.data['date_accueil']
        patient.contact = request.data['contact']
        patient.save()
        res = {'status': 'success', "message": "Mis à jour des infos réussi"}
    except ValidationError:
        res = {'status': 'error', 'message': "Patient introuvable introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)

# DELETE PATIENT
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePatient(request, id):
    try:
        Patient = Patient.objects.get(personneID=id)
        Patient.delete()
        res = {'status': 'success', 'message': 'Suppression d\'un Patient réussi'}
    except ValidationError:
        res = {'status': 'warning', 'message': "Patient introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)