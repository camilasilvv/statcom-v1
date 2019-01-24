from tkinter import *
import satellite
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import json
import time

class NewSatellitePage:
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

        # create variable for the down link entries
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
        # TODO : connect the save button to a function that will save the satellite in the database

        #creates the owner name box and modulation box
        self.labelOwner = Label(self.master,text="owner")
        self.boxOwner = Entry(self.master)
        self.labelModulation = Label(self.master, text="Modulation")
        self.boxModulation = Entry(self.master)

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
        self.saveBtn.grid(row=8, column=6)
        self.labelName.grid(row=0, column=0)
        self.nameBox.grid(row=0, column=1)


    def save(self):
        name=self.nameBox.get()
        upFreq=self.upFreqBox.get()
        downFreq=self.downFreqBox.get()
        owner=self.boxOwner.get()
        modulation=self.boxModulation.get()

        #verify if all the information is here
        if name=="" or upFreq==0 or downFreq==0 or owner=="" or modulation=="":

            self.errortext.set("all fields must be filled!")

        else:
            sat = satellite.Satellite(name=name, upFreq=upFreq, downFreq=downFreq, upBand="UHF", downBand="VHF",
                                      owner=owner, modulation=modulation)
            sat.saveInDB()




class NewReservationPage():
    def __init__(self, master):
        # window creation
        self.master = master
        self.master.title("new reservation")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text= "New reservation")
        self.labelNext = Label(self.master, text="Next passages")
        self.searchStatus = StringVar()
        self.labelStatus=Label(self.master, textvariable= self.searchStatus)

        self.labelSatName = Label(self.master, text= "Satellite name")
        self.boxSatellite= Entry(self.master)
        self.btnSearch= Button(self.master, text="search",command=self.searchSatellite)


        self.btnBrowser= Button(self.master, text="browse command file", command=self.OpenFile,width=18)

        self.availableList=Listbox(self.master)

        # place the widget in the frame
        self.labelTitle.grid(row=0, column =1)
        self.labelStatus.grid(row=2,column=1)
        self.labelNext.grid(row=3, column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)
        self.btnBrowser.grid(row=5,column=1)
        self.availableList.grid(row=4,column=1)

    def OpenFile(self):
         name = askopenfilename(initialdir="../../../Documents",
                                filetypes =(("Text File", "*.txt"), ("All Files", "*.*")),
                                title="Choose a file."
                                )
        # TODO: complete...
    def searchSatellite(self):
        found = False
        jsonSat= open("satelliteDB.json")
        satelliteList=json.load(jsonSat)
        self.searchStatus.set('satellite not found')
        for i in satelliteList:
            if i['name']==self.boxSatellite.get():
                self.searchStatus.set('satellite found')
                print("satellite found")
                found =True
        if found:
        # TODO : erase those
            self.availableList.insert(END,"2020_02_26@22_55_00")
            self.availableList.insert(END, "2020_03_26@19_45_00")
            self.availableList.insert(END, "2020_04_26@09_15_00")
            self.availableList.insert(END, "2020_05_26@15_45_00")
            self.availableList.insert(END, "2020_06_26@21_53_00")
        # TODO : print the time of reservation available(5) in the listbox (with predict)


class GetDataPage():
    def __init__(self, master):
        # window creation
        self.master = master
        self.master.title("Get data")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text="Get Data")
        self.labelAvailable = Label(self.master, text="Data available")
        self.labelSatName = Label(self.master, text="Satellite name")
        self.boxSatellite = Entry(self.master)
        self.btnSearch = Button(self.master, text="search")
        # TODO: connect this button to a function that will search the satellite in the database and open the data file

        self.searchStatus = StringVar()
        self.labelStatus = Label(self.master, textvariable=self.searchStatus)

        self.dataList=Listbox(self.master)

        self.btnDownload=Button(self.master,text="Download",width=15)
        # TODO : connect this button to a download function

        # place the widget in the frame

        self.labelTitle.grid(row=0, column=1)
        self.labelAvailable.grid(row=3, column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)
        self.labelStatus.grid(row=2,column=1)
        self.dataList.grid(row=4,column=1)
        self.btnDownload.grid(row=5,column=1)

    def searchSatellite(self):
        found = False
        jsonSat = open("satelliteDB.json")
        satelliteList = json.load(jsonSat)
        self.searchStatus.set('satellite not found')
        for i in satelliteList:
            if i['name'] == self.boxSatellite.get():
                self.searchStatus.set('satellite found')
                print("satellite found")
                found = True

class ManageSatellite:

    def __init__(self, master):

        self.master=master
        self.master.title("Satellite manager")

        self.listSatellite=Listbox(self.master)
        self.listSatellite.grid(column= 0, row=0)
        self.deleteBtn=Button(self.master,text='delete')
        self.deleteBtn.grid(column= 0, row=1)
        self.printSatellite()

    def printSatellite(self):
        jsonFile=open("./satelliteDB.json")
        allSatellites=json.load(jsonFile)
        print(allSatellites[0])
        for i in allSatellites:
            self.listSatellite.insert(END,i["name"])

class ManageReservation:
    def __init__(self, master):
        self.master=master
        self.master.title("Reservation manager")

        self.listReservation = Listbox(self.master,width=60)
        self.listReservation.grid(column=0, row=0)
        self.deleteBtn = Button(self.master, text='delete')
        self.deleteBtn.grid(column=0, row=1)
        self.printReservation()

    def printReservation(self):
        jsonFile = open("./reservationDB.json")
        allReservation= json.load(jsonFile)
        for i in allReservation:
            self.listReservation.insert(END, i["date"]+" by " +i["client"]+" for "+i['name'])


class ManageData:
    def __init__(self, master):
        self.master=master
        self.master.title("Data manager")
        self.listData = Listbox(self.master, width = 40)
        self.listData.grid(column=0, row=0)
        self.deleteBtn = Button(self.master, text='delete')
        self.deleteBtn.grid(column=0, row=1)
        self.printData()

    def printData(self):
        jsonFile = open("./dataDB",)
        allData= json.load(jsonFile)
        for i in allData:
            self.listData.insert(END, i["mission"]+" - "+i['date'])

class mainWindow:
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
        self.menu1.add_command(label="exit")

        self.menubar.add_cascade(label="File",menu=self.menu1)
        self.menu2.add_command(label="manage satellite",command=self.openManageSatellite)
        self.menu2.add_command(label="manage reservation", command=self.openManageReservation)
        self.menu2.add_command(label="manage data", command=self.openManageData)
        self.menubar.add_cascade(label="Edit", menu=self.menu2)

        self.menubar.add_command(label="help")
        
        self.master.config(menu=self.menubar)
        self.master.mainloop()
        #imgFile=open("Logo_mission.jpg")
        #img = ImageTk.PhotoImage(imgFile)
        #self.polyOrbite=Label(self.master,image=img)
        #self.polyOrbite.pack()

    def openNewSatellite(self):
         root2= Toplevel(self.master)
         newSatellitepage=NewSatellitePage(root2)

    def openNewreservation(self):
         root2= Toplevel(self.master)
         newSatellitePage=NewReservationPage(root2)

    def openGetData(self):
        root2 = Toplevel(self.master)
        getDataPage = GetDataPage(root2)


    def openManageSatellite(self):
         root2= Toplevel(self.master)
         newSatellitepage=ManageSatellite(root2)

    def openManageReservation(self):
         root2= Toplevel(self.master)
         newSatellitePage=ManageReservation(root2)

    def openManageData(self):
        root2 = Toplevel(self.master)
        getDataPage = ManageData(root2)


def main():
    root=Tk()
    firstPage= mainWindow(root)
    root.mainloop()


main()
