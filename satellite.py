import json
import shutil
import os
from pathlib import Path

class Satellite():
    def __init__(self, name, upFreq, downFreq, upBand, downBand, owner, modulation):
        self.name=name
        self.upFreq=upFreq
        self.downFreq=downFreq
        self.upBand=upBand
        self.downBand=downBand
        self.owner=owner
        self.modulation=modulation

    def saveInDB(self):

        #check if file exist
        file= Path("./satelliteDB.json")
        if file.exists():
            previousJson=open("./satelliteDB.json")
        else:
            previousJson = open("./satelliteDB.json",'w')
        #check if file is empty
        if os.stat("./satelliteDB.json").st_size==0:
            satelliteList=[]
        else:
            satelliteList=json.load(previousJson)


        dict = {
            'name':self.name,
            'upFreq':self.upFreq,
            'downFreq:' : self.downFreq,
            'upBand': self.upBand,
            'downBand':self.downBand,
            'owner':self.owner,
            'modulation':self.modulation
        }

        satelliteList.append(dict)
        jsonDB=json.dumps(satelliteList)


        with open('satelliteDB.json', 'w') as satDB:
            satDB.write(jsonDB)

    def dictToSatellite(self, dict):

        self.name = dict['name']
        self.upFreq = dict['upFreq']
        self.downFreq = dict['downFreq']
        self.upBand = dict['upBand']
        self.downBand = dict['downBand']
        self.owner = dict['owner']
        self.modulation = dict['modulation']


