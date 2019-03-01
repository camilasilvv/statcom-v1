from tkinter import *
from tkinter import messagebox
import satellite
import Reservation
from tkinter.filedialog import askopenfilename
# from PIL import ImageTk, Image
import json
import time
import os
import subprocess
import signal


class NewSatellitePage:

    '''
    ---------------------------------------------------------
    description: initialisation of the new Satellite page,
    this function initialize the variables and widgets of the page

    create by: Simon Belanger
    Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
    '''
    def __init__(self, master):

        # window creation
        self.master = master
        self.master.title("new satellite")
        self.frame=Frame(master)


        # create de widget for the satellite name
        self.labelName = Label(self.master, text="Satellite name")
        self.nameBox = Entry(self.master, text = "name")

        # create variable for the up link entries
        self.uplinkBand = StringVar()

        # create widget for the up link transmission
        self.upVHF = Radiobutton(self.master, text="VHF", variable = self.uplinkBand, value = 1)
        self.upUHF = Radiobutton(self.master, text="UHF", variable = self.uplinkBand, value = 2)
        self.upFreqBox = Spinbox(self.master, from_= 0, to= 600)
        self.labelUpLink = Label(self.master, text="uplink")

        # create variable for the down link entry
        self.downlinkBand = StringVar()

        # create widget for the down link transmission
        self.downVHF = Radiobutton(self.master, text="VHF", variable = self.downlinkBand, value = 1)
        self.downUHF = Radiobutton(self.master, text="UHF", variable = self.downlinkBand, value = 2)
        self.downFreqBox = Spinbox(self.master, from_= 0, to= 600)
        self.labelDownLink = Label(self.master, text="downlink")

        #create the save button widget
        self.saveBtn = Button(self.master,text="save",command=self.save)
        #create a error box
        self.errortext=StringVar()
        self.error=Label(self.master,textvariable=self.errortext)

        #creates the owner name box and modulation box
        self.labelOwner = Label(self.master,text="owner")
        self.boxOwner = Entry(self.master)
        self.labelModulation = Label(self.master, text="Modulation")
        self.boxModulation = Entry(self.master)

        #create a widget for TLE
        self.labelTLE=Label(self.master, text="TLE parameters")
        self.boxTLE = Entry(self.master)
        self.boxTLE2= Entry(self.master)

        # place the widgets
        self.labelUpLink.grid(row=1, column=0, rowspan=2)
        self.upVHF.grid(row=1, column=1)
        self.upUHF.grid(row=2, column=1)
        self.upFreqBox.grid(row=1, column =2,rowspan=2)

        self.labelDownLink.grid(row=3, column=0, rowspan=2)
        self.downVHF.grid(row=3, column=1)
        self.downUHF.grid(row=4, column=1)
        self.downFreqBox.grid(row=3, column=2,rowspan=2)

        self.labelOwner.grid(row=5, column=0)
        self.boxOwner.grid(row=5, column=1)
        self.labelModulation.grid(row=6, column= 0)
        self.boxModulation.grid(row=6, column=1)

        self.error.grid(row=7, column=1)
        self.saveBtn.grid(row=9, column=3)
        self.labelName.grid(row=0, column=0)
        self.nameBox.grid(row=0, column=1)
        self.boxTLE.grid(row=8, column= 1)
        self.boxTLE2.grid(row=9, column=1)
        self.labelTLE.grid(row=8,column=0, rowspan=2)

    '''
     ---------------------------------------------------------
    description: This function saves the satellite caracteristics to the 
    Database named satelliteDB.json

    create by: Simon Belanger 
    Last mmodified by : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''
    def save(self):

        # capture every entry made by the user
        name=self.nameBox.get()
        upFreq=self.upFreqBox.get()
        downFreq=self.downFreqBox.get()
        owner=self.boxOwner.get()
        modulation=self.boxModulation.get()

        #verify if all the information is here
        if name=="" or upFreq==0 or downFreq==0 or owner=="" or modulation=="":

            self.errortext.set("all fields must be filled!")

        else:

            try:
                if float(upFreq) > 500 or float(upFreq) < 100 or float(downFreq) > 500 or float(downFreq) < 100:
                    self.errortext.set("Frequencies not in range")
                else:
                    #saves the satellite in the database
                    sat = satellite.Satellite(name=name, upFreq=upFreq, downFreq=downFreq, upBand="UHF", downBand="VHF",
                                              owner=owner, modulation=modulation)
                    sat.saveInDB()
                    #save the TLE in predict TLE
                    TLEDB = open("/home/simon/.predict/predict.tle", 'a')
                    newTLE= name+"\n"+self.boxTLE.get()+"\n"+self.boxTLE2.get()+'\n'
                    TLEDB.write(newTLE)
                    # quit the window without closing the program
                    self.master.destroy()
            except ValueError:
                self.errortext.set("frequencies should be numbers")


class NewReservationPage:
    '''
     ---------------------------------------------------------
    description: initialisation of the new reservation page,
    this function initialize the variables and widgets of the page

    create by: Simon Belanger
    Last mmodified by : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''
    def __init__(self, master):
        # window creation
        self.master = master
        self.timeList=[]
        self.timeListUTC=[]
        self.lenghtList=[]
        self.frequencies=[]
        self.master.title("new reservation")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text= "New reservation")
        self.searchStatus = StringVar()
        self.labelStatus=Label(self.master, textvariable= self.searchStatus)
        self.labelSatName = Label(self.master, text= "Satellite name")
        self.boxSatellite= Entry(self.master)
        self.btnSearch= Button(self.master, text="search",command=self.searchSatellite)

        #creates the widget to search the command file
        self.btnBrowser= Button(self.master, text="browse command file", command=self.OpenFile,width=18)
        self.commandName=StringVar()
        self.boxCommandName= Entry(self.master,textvariable=self.commandName)


        #creates widgets for the next passage list
        self.labelNext = Label(self.master, text="Next passages")
        self.availableList=Listbox(self.master, selectmode=MULTIPLE, width=40)

        #creates the button to save the reservation
        self.btnSave = Button(self.master, text="save", command = self.save)


        # place the widget in the frame
        self.labelTitle.grid(row=0, column =1)
        self.labelStatus.grid(row=2,column=1)
        self.labelNext.grid(row=3, column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)
        self.btnBrowser.grid(row=5,column=2)
        self.boxCommandName.grid(row=5, column=0,columnspan=2 )
        self.availableList.grid(row=4,column=1)
        self.btnSave.grid(row=6,column=2)


    '''
     ---------------------------------------------------------
    description: this function makes the user search for his command file
    and capture the name of the file when the browse button is pressed

    create by: Simon Belanger 
    Last mmodified by : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''
    def OpenFile(self):

        # open the file viewer
        cmd = askopenfilename(initialdir="../../../Documents", filetypes =(("Wave File", "*.wav"), ("All Files", "*.*")),title="Choose a file.")

        self.commandName.set(cmd)

    def save(self):

        selection = self.availableList.curselection()
        #check if fields are empty
        if not selection:
            self.searchStatus.set("All field must be filled!")
        else:
            for i in range(len(self.availableList.curselection())):
                print(selection[i])
                print(self.timeList[selection[i]])
                reservation=Reservation.Reservation(satellite=self.boxSatellite.get(), reservationTime = self.timeList[selection[i]],length=self.lenghtList[selection[i]], client ="polyorbite", data=self.boxCommandName.get(), frequencies=self.frequencies, timeUTC=int(self.timeListUTC[selection[i]]) )
                reservation.saveInDB()
            self.master.destroy()
    '''
     ---------------------------------------------------------
    @newfield brief: Description
    @brief: This function searches the satellite in the database
    and print out the next passages in the listbox widget

    @author: Simon Belanger 
    @date : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''
    def searchSatellite(self):

        found = False
        # verify if the satellite is in the database
        if os.path.isfile('./satelliteDB.json'):

            # open the json file and convert it to a python list
            jsonSat= open("satelliteDB.json")
            satelliteList=json.load(jsonSat)

            #update the search status
            self.searchStatus.set('satellite not found')
            for i in satelliteList:
                if i['name']==self.boxSatellite.get():
                    self.searchStatus.set('satellite found')
                    self.frequencies.append(i['upFreq'])
                    self.frequencies.append(i['downFreq'])
                    print("satellite found")
                    found =True

            # print the next passages if the satellite is found
            if found:
            # TODO : erase those
                #self.timeList=["2020_02_26@22_55_00","2020_03_26@19_45_00", "2020_03_26@19_45_00", "2020_05_26@15_45_00", "2020_06_26@21_53_00"]
                nextTime=str(int(time.time()))

                for i in range(5):
                    nextPass=self.getPassages(nextTime)
                    print(nextPass)
                    self.timeListUTC.append(nextPass[0])
                    self.timeList.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(nextPass[0]))))
                    self.lenghtList.append(int(nextPass[1])-int(nextPass[0]))
                    self.availableList.insert(END, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(nextPass[0])))+'->'+str(int(nextPass[1])-int(nextPass[0])))
                    nextTime=str(int(nextPass[1])+30)
                    print(nextTime)

            # TODO : print the time of reservation available(5) in the listbox (with predict)
        else:
            self.searchStatus.set("database not found")

    '''
        ---------------------------------------------------------
       @newfield brief: Description
       @brief: Searches the next passages with predict

       @author: Simon Belanger 
       @date : Simon Belanger @2019-01-24
        ---------------------------------------------------------
       '''
    def getPassages(self, time):
        cmd = ['predict', '-p', self.boxSatellite.get(), time]

        # executes the cmd and capture the output
        output = subprocess.Popen(cmd, stdout = subprocess.PIPE).communicate()[0]

        #convert bytes to string
        strCmd=output.decode("utf-8")

        #split to have a single line
        strLine= strCmd.split('\n')

        #split to have two single times
        strTimeBegin=strLine[0].split(' ')
        strTimeEnd=strLine[len(strLine)-2].split(' ')

        return [strTimeBegin[0],strTimeEnd[0]]


class GetDataPage():
    '''
     ---------------------------------------------------------
    description: initialisation of the get Data page,
    this function initialize the variables and widgets of the page

    create by: Simon Belanger
    Last mmodified by : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''

    def __init__(self, master):
        # window creation
        self.master = master
        self.master.title("Get data")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text="Get Data")
        self.labelSatName = Label(self.master, text="Satellite name")
        self.boxSatellite = Entry(self.master)
        self.btnSearch = Button(self.master, text="search", command=self.searchSatellite)
        self.searchStatus = StringVar()
        self.labelStatus = Label(self.master, textvariable=self.searchStatus)

        # creates widget for the list of data available
        self.dataList=Listbox(self.master,width=30)
        self.labelAvailable = Label(self.master, text="Data available")
        self.btnDownload=Button(self.master,text="Download",width=15, command=self.downloadData)
        self.downloadList=[]

        # place the widget in the frame

        self.labelTitle.grid(row=0, column=1)
        self.labelAvailable.grid(row=3, column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)
        self.labelStatus.grid(row=2,column=1)
        self.dataList.grid(row=4,column=1)
        self.btnDownload.grid(row=5,column=1)


    '''
     ---------------------------------------------------------
    description: This function searches the satellite in the database
    and print out the next passages in the listbox widget

    create by: Simon Belanger 
    Last mmodified by : Simon Belanger @2019-01-24
     ---------------------------------------------------------
    '''
    def searchSatellite(self):

        found = False

        # verify if the satellite is in the database
        if os.path.isfile('./dataDB'):

            # convert the json file to a python list
            jsonSat = open("dataDB")
            DataList = json.load(jsonSat)


            self.searchStatus.set('satellite not found')
            for i in DataList:
                if i["satellite"] == self.boxSatellite.get():
                    self.searchStatus.set('satellite found')
                    print("satellite found")
                    found = True
                    self.dataList.insert(END, i["mission"]+" - " +i['date'])
                    self.downloadList.append(i["file name"])

            # TODO: print the file names available for download
        else:
            self.searchStatus.set("database not found")

    def downloadData(self):

        # verify if the satellite is in the database
        selection = self.dataList.curselection()
        if len(selection)==0:
            self.searchStatus.set("choose a file")
        else:
            if os.path.isfile('./dataDB'):

                # convert the json file to a python list
                jsonSat = open("dataDB")
                DataList = json.load(jsonSat)

                selection = self.dataList.curselection()
                for i in selection:

                    os.rename(self.downloadList[i], "/home/simon/Documents/"+self.downloadList[i].replace("/home/simon/Downloads/", ""))
                self.master.destroy()
            else:
                self.searchStatus.set('Database not found')




class ManageSatellite:

    '''
    ---------------------------------------------------------
   description: initialisation of the get manage satellite page,
   this function initialize the widgets of the page

   create by: Simon Belanger
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
    '''
    def __init__(self, master):

        self.master=master
        self.master.title("Satellite manager")

        self.listSatellite=Listbox(self.master)
        self.listSatellite.grid(column= 0, row=0)
        self.deleteBtn=Button(self.master,text='delete', command=self.delete)
        self.deleteBtn.grid(column= 0, row=1)
        self.printSatellite()

    def delete(self):

        previousJson = open("./satelliteDB.json")
        satelliteList=[]
        satelliteList = json.load(previousJson)
        selection =self.listSatellite.curselection()
        for i in range(len(selection)):
            satelliteList.pop(selection[i])
            self.listSatellite.delete(selection[i])

        jsonDB = json.dumps(satelliteList)
        with open('satelliteDB.json', 'w') as satDB:
            satDB.write(jsonDB)

    '''
        ---------------------------------------------------------
       description: show all the satellite registered 

       create by: Simon Belanger 
       Last mmodified by : Simon Belanger @2019-01-24
        ---------------------------------------------------------
       '''
    def printSatellite(self):

        # verify if the satellite is in the database
        if os.path.isfile('./satelliteDB.json'):

            # convert the json file to a python list
            jsonFile=open("./satelliteDB.json")
            allSatellites=json.load(jsonFile)
            print(allSatellites[0])
            for i in allSatellites:
                self.listSatellite.insert(END,i["name"])
        else:
            print("database not found \n")

class ManageReservation:
    '''
    ---------------------------------------------------------
   description: initialisation of the get manage reservation page,
   this function initialize the widgets of the page

   create by: Simon Belanger
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def __init__(self, master):
        self.master=master
        self.master.title("Reservation manager")

        self.listReservation = Listbox(self.master,width=60)
        self.listReservation.grid(column=0, row=0)
        self.deleteBtn = Button(self.master, text='delete',command=self.delete)
        self.deleteBtn.grid(column=0, row=1)
        self.printReservation()

    '''
    ---------------------------------------------------------
   description: show all the reservations taken 

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def printReservation(self):

        # verify if the satellite is in the database
        if os.path.isfile('./reservationDB.json'):

            # convert the json file to a python list
            jsonFile = open("./reservationDB.json")
            allReservation= json.load(jsonFile)
            for i in allReservation:
                self.listReservation.insert(END, i["reservationTime"]+" by " +i["client"]+" for "+i["satellite"])
        else:
            print("database not found \n")

    def delete(self):

        previousJson = open("./reservationDB.json")
        reservationList=[]
        reservationList = json.load(previousJson)
        selection =self.listReservation.curselection()
        for i in range(len(selection)):
            reservationList.pop(selection[i])
            self.listReservation.delete(selection[i])

        jsonDB = json.dumps(reservationList)
        with open('reservationDB.json', 'w') as resDB:
            resDB.write(jsonDB)


class ManageData:
    '''
    ---------------------------------------------------------
   description: initialisation of the get manage Data page,
   this function initialize the widgets of the page

   create by: Simon Belanger
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def __init__(self, master):
        self.master=master
        self.master.title("Data manager")
        self.listData = Listbox(self.master, width = 40)
        self.listData.grid(column=0, row=0)
        self.deleteBtn = Button(self.master, text='delete', command=self.delete)
        self.deleteBtn.grid(column=0, row=1)
        self.printData()

    '''
    ---------------------------------------------------------
   description: show all the data available 

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def printData(self):
        jsonFile = open("./dataDB",)
        allData= json.load(jsonFile)
        for i in allData:
            self.listData.insert(END, i["mission"]+" - "+i['date'])

    def delete(self):

        previousJson = open("./dataDB")

        dataList = json.load(previousJson)
        selection =self.listData.curselection()
        for i in range(len(selection)):
            dataListList.pop(selection[i])
            self.listData.delete(selection[i])

        jsonDB = json.dumps(dataList)
        with open('dataDB', 'w') as dataDB:
            dataDB.write(jsonDB)


class mainWindow:
    '''
    ---------------------------------------------------------
   description: initialisation of the main page,
   this function initialize the widgets of the page

   create by: Simon Belanger
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def __init__(self, master):
        self.master = master
        
        self.master.title("statcom")

        self.menubar=Menu(self.master)

        self.menu1=Menu(self.menubar,tearoff =0)
        self.menu2 = Menu(self.menubar, tearoff=0)

        self.menu1.add_command(label="new satellite", command=self.openNewSatellite)
        self.menu1.add_command(label="new reservation", command = self.openNewreservation)
        self.menu1.add_command(label="get data", command = self.openGetData)
        self.menu1.add_separator()

        self.menu1.add_command(label="exit", command = self.on_closing)


        self.menubar.add_cascade(label="File",menu=self.menu1)
        self.menu2.add_command(label="manage satellite",command=self.openManageSatellite)
        self.menu2.add_command(label="manage reservation", command=self.openManageReservation)
        self.menu2.add_command(label="manage data", command=self.openManageData)
        self.menu2.add_command(label="update SDR", command=self.update_SDR)
        self.menubar.add_cascade(label="Edit", menu=self.menu2)

        self.menubar.add_command(label="help")

        self.gpredict_pid = subprocess.Popen("gpredict &", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        self.predict_udp = subprocess.Popen("predict -s &", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.master.config(menu=self.menubar)
        #creates widget for printing the next reservation time
        self.updateBtn = Button(self.master, text='update', command=self.update).grid(row=0,column=0)
        self.nextReservation= StringVar()
        self.title= Label(self.master, text='Next passage').grid(row=1,column=0)
        #self.reservationTable=Label(self.master, text='nextReservation')
        self.reservationTable = Label(self.master, textvariable=self.nextReservation).grid(row=2, column=0)


        self.master.mainloop()


    def update(self):
        # verify if the satellite is in the database
        if os.path.isfile('./reservationDB.json'):

            # convert the json file to a python list
            jsonFile = open("./reservationDB.json")
            allReservation = json.load(jsonFile)
            self.nextReservation.set('')
            for i in allReservation:

                self.nextReservation.set(self.nextReservation.get() + i["reservationTime"] + " by " + i["client"] + " for " + i["satellite"]+'\n')


        else:
            self.nextReservation='database not found'


    '''
    ---------------------------------------------------------
   description: open the new satellite page

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def openNewSatellite(self):
         root2= Toplevel(self.master)
         newSatellitepage=NewSatellitePage(root2)

    '''
    ---------------------------------------------------------
   description: open the new reservation page

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def openNewreservation(self):
         root2= Toplevel(self.master)
         newSatellitePage=NewReservationPage(root2)

    '''
    ---------------------------------------------------------
   description: open the new get data page

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def openGetData(self):
        root2 = Toplevel(self.master)
        getDataPage = GetDataPage(root2)

    '''
        ---------------------------------------------------------
       description: open the new manager page

       create by: Simon Belanger 
       Last mmodified by : Simon Belanger @2019-01-24
        ---------------------------------------------------------
       '''
    def openManageSatellite(self):
         root2= Toplevel(self.master)
         newSatellitepage=ManageSatellite(root2)

    '''
    ---------------------------------------------------------
   description: open the reservation manager page

   create by: Simon Belanger 
   Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
   '''
    def openManageReservation(self):
         root2= Toplevel(self.master)
         newSatellitePage=ManageReservation(root2)

    '''
    ---------------------------------------------------------
    description: open the data manager page

    create by: Simon Belanger 
    Last mmodified by : Simon Belanger @2019-01-24
    ---------------------------------------------------------
    '''
    def openManageData(self):
        root2 = Toplevel(self.master)
        getDataPage = ManageData(root2)

    '''
    ---------------------------------------------------------
    description: Update LimeSDR

    create by: Emile Cote Pelletier
    Last mmodified by : Emile Cote Pelletier @2019-02-17
    ---------------------------------------------------------
    '''
    def update_SDR(self):
        update = os.system("LimeUtil --update")
        if update != 0:
        	messagebox.showerror("SDR Update","No Device connected")
       	else:	
       		messagebox.showinfo("SDR Update","Device Updated !")
    '''
	---------------------------------------------------------
    description: Close backprocess when closing the app

    create by: Emile Cote Pelletier
    Last mmodified by : Emile Cote Pelletier @2019-02-17
    ---------------------------------------------------------
    '''	
    def on_closing(self):
    	os.killpg(os.getpgid(self.gpredict_pid.pid), signal.SIGTERM)
    	os.killpg(os.getpgid(self.predict_udp.pid), signal.SIGTERM)
    	self.master.destroy()


def main():

    root=Tk()
    firstPage= mainWindow(root)
    firstPage.update()

    root.mainloop()


main()
