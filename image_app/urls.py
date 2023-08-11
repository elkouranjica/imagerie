from django.urls import path

from image_app.views  import personne_views as PersonneViews , agent_views as AgentViews, patient_views as PatientViews, imagerie_views as ImagerieViews, resultat_views as ResultatViews

urlpatterns = [
   
    #PERSONNE URLS
    path('personne/', PersonneViews.allPersonnes),
    path('personne/<id>/', PersonneViews.getpersonneById),
    path('personne/add', PersonneViews.addPersonne),
    path('personne/<id>/update', PersonneViews.updatePersonne),
    path('personne/<id>/delete', PersonneViews.deletePersonne),

    #AGENT
    path('agent/', AgentViews.allAgents),
    path('agent/<id>/', AgentViews.getAgentById),
    path('agent/add', AgentViews.addAgent),
    path('agent/<id>/update', AgentViews.updateAgent),
    path('agent/<id>/delete', AgentViews.deleteAgent),
    
    #PATIENTS
    path('patient/', PatientViews.allPatients),
    path('patient/<id>/', PatientViews.getPatientById),
    path('patient/add', PatientViews.addPatient),
    path('patient/<id>/update', PatientViews.updatePatient),
    path('patient/<id>/delete', PatientViews.deletePatient),

    #IMAGERIE
    path('image/', ImagerieViews.allImageries),
    path('image/<id>/', ImagerieViews.getImagerieById),
    path('image/add', ImagerieViews.addImagerie),
    path('image/<id>/update', ImagerieViews.updateImagerie),
    path('image/<id>/delete', ImagerieViews.deleteImagerie),
   
    #RESULTATS
    path('resultat/', ResultatViews.allResultats),
    path('resultat/<id>/', ResultatViews.getResultatById),
    path('resultat/add', ResultatViews.addResultat),
    path('resultat/<id>/update', ResultatViews.updateResultat),
    path('resultat/<id>/delete', ResultatViews.deleteResultat),
]
