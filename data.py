import json

class Data():
    def __init__(self, receivedData, commandData):
        self.receivedData= commandData
        self.commandData = commandData

        # todo :1 implemet communication with sdr to create/get WAV files