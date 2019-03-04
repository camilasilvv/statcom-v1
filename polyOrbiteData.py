import datetime
import os
'''
   ---------------------------------------------------------
   description: this code sorts and stores the data received in an AX.25 into a DB for PolyOrbite
   created by: Camila Silveira
   Last mmodified by : Camila Silveira @2019-03-04
   ---------------------------------------------------------
   '''

class PolyOrbiteData():
    def __init__(self, binFile):
        self.binFile : binFile


'''
   ---------------------------------------------------------
   description: this function function checks if there is already a file created for this week, if not, it creates one
   created by: Camila Silveira
   Last mmodified by : Camila Silveira @2019-03-04
   ---------------------------------------------------------
   '''
def createJSON():
    launch = datetime.date(2019, 2, 18) # example for testing, replace with the real launch date
    week = (datetime.date.today()-launch).days//7
    file = './S'+str(week)+'.json'
    if os.path.isfile(file) is False:
        f = open(file, "w+")
        f.close()


createJSON()
'''
   ---------------------------------------------------------
   description: this function extracts the data from the binary file and saves it into the json file
   created by: Camila Silveira
   Last mmodified by : Camila Silveira @2019-03-04
   ---------------------------------------------------------
   '''
