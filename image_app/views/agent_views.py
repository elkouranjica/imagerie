from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from image_app.serializers import AgentSerializer
from image_app.models import Agent
from django.core.exceptions import ValidationError

# GET PERSONNE 
@api_view(['GET'])
@permission_classes([IsAdminUser])
def allAgents(request):
    try:
        agent = Agent.objects.all()
        serialisation = AgentSerializer(agent, many=True)
        res = serialisation.data
    except: 
        res = {'status': 'warning', 'message': 'Une erreur c\'est produite, essayez plus tard'}
    return Response(res)

# GET PERSONNE  BY ID
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAgentById(request, id):
    try:
        agent = Agent.objects.get(agentID=id)
        serialisation = AgentSerializer(agent, many=False)
        res = serialisation.data
    except ValidationError:
        res = {'status': 'error', 'message': 'Identifiant Invalide'}
    except:
        res = {'status': 'warning', 'message': 'Donnee introuvable'}
    return Response(res)

# ADD NEW ANNEE UNIV
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addAgent(request):
    try:
        serialisation = AgentSerializer(data=request.data, many=False)
        res = None;
        if serialisation.is_valid():
            serialisation.save()
            res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'une agent effectuée' }
        else:
            res = {'status': 'warning', 'message': "Entreés invalides"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res);


# UPDATE PERSONNE
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateAgent(request, id):
    try:
        agent = Agent.objects.get(agent=id);
        agent.date_accueil = request.data['date_accueil']
        agent.contact = request.data['contact']
        agent.save()
        res = {'status': 'success', "message": "Mis à jour des infos réussi"}
    except ValidationError:
        res = {'status': 'error', 'message': "Agent introuvable introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)

# DELETE PERSONNE
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAgent(request, id):
    try:
        Agent = Agent.objects.get(personneID=id)
        Agent.delete()
        res = {'status': 'success', 'message': 'Suppression d\'un Agent réussi'}
    except ValidationError:
        res = {'status': 'warning', 'message': "Agent introuvable"}
    except:
        res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
    return Response(res)