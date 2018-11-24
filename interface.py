import json
import time

# while True:
#
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

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)