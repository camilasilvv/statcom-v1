from tkinter import *


def new_observation():


    window2=Toplevel(window1)
    window2.title("new observation")

    uplinkBand = StringVar()
    upFreq = DoubleVar()
    upVHF = Radiobutton(window2, text="VHF", variable = uplinkBand, value = 1)
    upUHF = Radiobutton(window2, text="UHF", variable = uplinkBand, value = 2)
    upFreqBox = Entry(window2)

    downlinkBand = StringVar()
    downFreq = DoubleVar()
    downVHF = Radiobutton(window2, text="VHF", variable = downlinkBand, value = 1)
    downUHF = Radiobutton(window2, text="UHF", variable = downlinkBand, value = 2)
    downFreqBox = Entry(window2)

    labelUpLink = Label(window2, text="uplink")
    labelDownLink = Label(window2, text="downlink")

    saveBtn = Button(window2,text="save")


    labelUpLink.grid(row=0, column=0, rowspan=2)
    upVHF.grid(row=0, column=1)
    upUHF.grid(row=1, column=1)
    upFreqBox.grid(row=0, column =2,rowspan=2)

    labelDownLink.grid(row=2, column=0, rowspan=2)
    downVHF.grid(row=2, column=1)
    downUHF.grid(row=3, column=1)
    downFreqBox.grid(row=2, column=2,rowspan=2)

    saveBtn.grid(row=6, column=6)





window1=Tk()
window1.title("statcom")

menubar=Menu(window1)

menu1=Menu(menubar,tearoff =0)

menu1.add_command(label="new observation",command=new_observation)
menu1.add_command(label="edit observation")
menu1.add_command(label="get data")
menu1.add_separator()
menu1.add_command(label="exit")

menubar.add_cascade(label="File",menu=menu1)
menubar.add_command(label="help")

window1.config(menu=menubar)
window1.mainloop()

