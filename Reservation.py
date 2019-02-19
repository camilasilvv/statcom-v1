import satellite
import time
import os
import json
from pathlib import Path

class Reservation:

    def __init__(self, satellite, reservationTime, length, client, data, frequencies):
        self.satellite = satellite
        self.reservationTime = reservationTime
        self.client=client
        # TOdO: add entry box for data
        self.length=length
        self.data = data
        self.frequencies=frequencies

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
            'reservationTime': self.reservationTime, #TODO: make sure that time units/formats are compatible
            'client': self.client,
            'length': self.length,
            'command file': self.data,
            'Uplink': self.frequencies[0],
            'Downlink': self.frequencies[1]
          # TODO : modify userWindow.py
        }

        reservationList.append(dict)

        #sorting the database by soonest reservation time
        reservationList = sorted(reservationList, key=lambda k: k['reservationTime'])

        jsonDB = json.dumps(reservationList)

        with open('reservationDB.json', 'w') as resDB:
            resDB.write(jsonDB)

        #todo:    2- make this an aggregation so that if the satellite is deleted, the reservation is as well
        #         3- fix the init of this class so that we have a command data (uplink) and received data (downlink)

