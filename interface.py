import json



# while True:
# test 1:
# 	## Enregistrer les donnees recues du SDR sur la base de donnees:
#
# 	# pour le test on utilise une donnee rentree par l'usager.
# 	# a remplacer avec donnees provenant du SDR
# 	# data = input('Donnee a entrer dans la BD: ')
# 	#with open('data.json', 'a') as outfile:
# 	#	json.dump(time.strftime("%d/%m/%Y %H:%M:%S")+ ' ' + data, outfile)
# 	#	outfile.write('\n')
# 	#print(time.strftime("%d/%m/%Y %H:%M:%S"), ' ', data)
# 	# format de la BD:
# 	# variable / date / heure / valeur
#
#
# 	## Filtrer les donnees de la BD et enregistrer les plus recentes sur le fichier latest.json
#
# 	# test pour remplir le fichier "latest.json"
# 	 #with open('latest.json', 'a') as outfile:
# 	#	for i in range(0, 34):
# 	#		json.dump(str(i) + " 123 00/00/2000 00:00:00", outfile)
# 	#		outfile.write('\n')
# 	# print ("done")
#
# 	# on lit les donnees dans la BD l'ecrit sur le fichier sorted_data.json
# 	# with open('data.json', 'a') as source:
# 	# 	data_source = json.load(source)
# 	# 	for
# 	# 	json.dump()
# 	# 	json_file.write("")
#
#
#
#
#
#
# 	print ("test")
#
# 	## Lecture du fichier latest pour affichage sur l'interface graphique
# 	# peut etre cela se fera sur un autre programme. A voir

# test 2:
#data = {}
#data['people'] = []
#data['people'].append({
#    'name': 'Scott',
#    'website': 'stackabuse.com',
#    'from': 'Nebraska'
#})
#data['people'].append({
 #   'name': 'Larry',
 #   'website': 'google.com',
 #   'from': 'Michigan'
#})
#data['people'].append({
#    'name': 'Tim',
###    'website': 'apple.com',
#    'from': 'Alabama'
#})
#
#with open('data.json', 'w') as outfile:
#    json.dump(data, outfile)
#
# def ConfigurationSDR():
#     # Cette fonction permet de configurer LimeSDR a partir des donnees entrees par l'usager
#
# def PositionAntenne():
#     # Cette fonction permet d'envoyer les parametres de suivi a l'Arduino pour le controle des moteurs
#
# def StoreData():
#     # Cette fonction permet d'enrgistrer les donnees recues dans la base de donnees, et de creer les fichiers de
#     # la base de donnees, le cas echeant
#
# def Receive():
#     # Cette fonction permet de recevoir les donnees decodees par LimeSDR et les enregistrer dans la base de donnees
#     # bloc provenant de LimeSDR
#     StoreData()
#
# def SendCommand():
#     # Cette fonction permet d'envoyer les commandes entrees par l'usager au SDR
#
# def ShowData():
#     # Cette fonction permet d'afficher les donnees les plus recentes des missions sur l'interface graphique.
#     # La fonction ouvre et lit les fichiers de donnees des deux dernieres semaines, et ensuite affiche la valeur la
#     # plus recentes de chaque varible
#     # a inserer bloc pour l'affichage dans l'interface
#
# def StreamCamera():
#     # Cette fonction permet d'initialiser la camera de surveillance, de recevoir et afficher la video en temps reel
#
# def GPredictMap():
#     # Cette fonction permet d'afficher la carte GPredict, bloc code open source
#
# def EntreeDonnesSDR():
#     # Cette fonction permet a l'usager d'entrer les parametres pour la configuration du SDR
#     # a regarder les parametres requis pour le suivi dans les bloc code de LimeSDR
#
# def TrackingTLE():
#     # Cette fonction permet a l'usager d'entrer les two-line element pour le suivi du satellite
#
# def EntreeCommands():
#     # Cette fonction permet a l'usager d'entrer les commandes a envoyer au satellite
#
# def ConfigurationInterface():
#     # Cette fonction permet de configurer l'environnement pour l'interface graphique
#     # a ajouter tous les blocs pour les entrees de commandes, parametres, etc