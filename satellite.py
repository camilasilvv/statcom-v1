import json
import shutil

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
        previousJson=open("./satelliteDB.json")
        satelliteList= json.load(previousJson)
        print(type(satelliteList))

        dict = {
            'name':self.name,
            'upFreq':self.upFreq,
            'downFreq:' : self.downFreq,
            'upBand': self.upBand,
            'downBand':self.downBand,
            'owner':self.owner,
            'modulation':self.modulation
        }
        jsonDB=json.dumps(dict)

        with open('satelliteDB.json', 'w') as satDB:
            satDB.write(jsonDB)

        #shutil.move("satelliteDB.json","/home/simon/Documents/satelliteDB.json")



#s= Satellite(name= "test",upFreq=440,downFreq=144,upBand="UHF",downBand="VHF",owner="statcom",modulation="FSK")
#s.saveInDB()
