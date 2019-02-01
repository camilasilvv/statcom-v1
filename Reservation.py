import satellite
import time

class Reservation:
    def __init__(self, satellite, reservationTime, client, data):
        self.satellite = satellite
        # self.date=date #CS: check if this change affects other functions. i changed this for:
        self.reservationTime = reservationTime
        self.client=client
        self.data = data

    def saveInDB(self):
        previousJson = open("./reservationDB.json")
        if os.stat("./satelliteDB.json").st_size == 0:
            reservationList = []
        else:
            reservationList = json.load(previousJson)
        print(type(reservationList))

        # to do : 1- set up udp connection to communicate with Predict
        #         2- make this an aggregation so that if the satellite is deleted, the reservation is as well
        #         3- fix the init of this class so that we have a command data (uplink) and received data (downlink)