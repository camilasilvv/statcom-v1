import satellite
import time

class Reservation:
    def __init__(self, satellite, date, client):
        self.satellite = satellite
        self.date=date
        self.client=client

     def saveInDB(self):
         previousJson = open("./reservationDB.json")
        if os.stat("./satelliteDB.json").st_size == 0:
            reservationList = []
        else:
            reservationList = json.load(previousJson)
        print(type(reservationList))