import satellite
import time
import os
import json
from pathlib import Path

class Reservation:

    def __init__(self, satellite, reservationTime, length, client, data):
        self.satellite = satellite
        self.reservationTime = reservationTime
        self.client=client
        # TOdO: add entry box for data
        self.length=length
        self.data = data

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
          # TODO : modify userWindow.py
        }

        reservationList.append(dict)
        jsonDB = json.dumps(reservationList)

        with open('reservationDB.json', 'w') as resDB:
            resDB.write(jsonDB)

        #todo: 1- set up udp connection to communicate with Predict
        #         2- make this an aggregation so that if the satellite is deleted, the reservation is as well
        #         3- fix the init of this class so that we have a command data (uplink) and received data (downlink)
