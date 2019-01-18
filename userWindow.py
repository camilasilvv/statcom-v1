from tkinter import *

class NewSatellitePage:
    def __init__(self, master):

        # window creation
        self.master = master
        self.master.title("new satellite")


        # create de widget for the satellite name
        self.labelName = Label(self.master, text="Satellite name")
        self.nameBox = Entry(self.master, text = "name")

        # create variable for the up link entries
        self.uplinkBand = StringVar()
        self.upFreq = DoubleVar()
        # create widget for the up link transmission
        self.upVHF = Radiobutton(self.master, text="VHF", variable = self.uplinkBand, value = 1)
        self.upUHF = Radiobutton(self.master, text="UHF", variable = self.uplinkBand, value = 2)
        # TODO : add all variables to the entries
        self.upFreqBox = Entry(self.master)

        self.labelUpLink = Label(self.master, text="uplink")

        # create variable for the down link entries
        self.downlinkBand = StringVar()
        self.downFreq = DoubleVar()

        # create widget for the down link transmission
        self.downVHF = Radiobutton(self.master, text="VHF", variable = self.downlinkBand, value = 1)
        self.downUHF = Radiobutton(self.master, text="UHF", variable = self.downlinkBand, value = 2)
        self.downFreqBox = Entry(self.master)

        self.labelDownLink = Label(self.master, text="downlink")

        #create the save button widget
        self.saveBtn = Button(self.master,text="save")
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


        self.saveBtn.grid(row=7, column=6)
        self.labelName.grid(row=0, column=0)
        self.nameBox.grid(row=0, column=1)


        
        # TODO : define a save function

class NewReservationPage():
    def __init__(self, master):
        # window creation
        self.master = master
        self.master.title("new reservation")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text= "New reservation")
        self.labelNext = Label(self.master, text="Next passages")
        self.labelSatName = Label(self.master, text= "Satellite name")
        self.boxSatellite= Entry(self.master)
        self.btnSearch= Button(self.master, text="search")
        # TODO: connect this button to a function that will search the satellite in the database and print the next passages

        # place the widget in the frame
        self.labelTitle.grid(row=0, column =1)
        self. labelNext.grid(row=2,column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)

class GetDataPage():
    def __init__(self, master):
        # window creation
        self.master = master
        self.master.title("new reservation")

        # create the widget for the search bar
        self.labelTitle = Label(self.master, text="Get Data")
        self.labelAvailable = Label(self.master, text="Data available")
        self.labelSatName = Label(self.master, text="Satellite name")
        self.boxSatellite = Entry(self.master)
        self.btnSearch = Button(self.master, text="search")
        # TODO: connect this button to a function that will search the satellite in the database and print all the data

        # place the widget in the frame

        self.labelTitle.grid(row=0, column=1)
        self.labelAvailable.grid(row=2, column=1)
        self.labelSatName.grid(row=1, column=0)
        self.boxSatellite.grid(row=1, column=1)
        self.btnSearch.grid(row=1, column=2)

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
        self.menu2.add_command(label="manage satellite")
        self.menu2.add_command(label="manage reservation")
        self.menu2.add_command(label="manage data")
        self.menubar.add_cascade(label="Edit", menu=self.menu2)

        self.menubar.add_command(label="help")
        
        self.master.config(menu=self.menubar)
        self.master.mainloop()



    def openNewSatellite(self):
         root2= Toplevel(self.master)
         newSatellitepage=NewSatellitePage(root2)

    def openNewreservation(self):
         root2= Toplevel(self.master)
         newSatellitePage=NewReservationPage(root2)

    def openGetData(self):
        root2 = Toplevel(self.master)
        getDataPage = GetDataPage(root2)



def main():
    root=Tk()
    firstPage= mainWindow(root)
    root.mainloop()


main()