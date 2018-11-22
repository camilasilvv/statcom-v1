import json
import time

while True:
	# pour le test on utilise une donnee rentree par l'usager. a remplacer avec donnees provenant du SDR
	data = input('Donnee a entrer dans la BD: ')
	with open('data.json', 'a') as outfile:
		json.dump(time.strftime("%d/%m/%Y %H:%M:%S")+ ' ' + data, outfile)
		outfile.write('\n')
	print(time.strftime("%d/%m/%Y %H:%M:%S"), ' ', data)
	
