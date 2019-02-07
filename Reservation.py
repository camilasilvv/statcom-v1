import satellite
import time
import os
import json
from pathlib import Path

class Reservation:
    def __init__(self, satellite, date, client, lenght,commandFileName):
        self.satellite = satellite
        self.date=date
        self.client=client
        self.lenght=lenght
        self.commandFileName=commandFileName

    def saveInDB(self):

        # check if file exist
        file = Path("./reservationDB.json")
        if file.exists():
            previousJson = open("./reservationDB.json")
        else:
            previousJson = open("./reservationDB.json", "w")
        if os.stat("./reservationDB.json").st_size == 0:
            reservationList = []
            print('empty json')
        else:
            reservationList = json.load(previousJson)
        print(type(reservationList))

        dict = {
            'satellite': self.satellite,
            'date': self.date,
            'client': self.client,
            'lenght': self.lenght,
            'command file': self.commandFileName,
        }

        reservationList.append(dict)
        jsonDB = json.dumps(reservationList)

        with open('reservationDB.json', 'w') as resDB:
            resDB.write(jsonDB)

