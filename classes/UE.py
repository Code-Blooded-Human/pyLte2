from classes.MeasurementReport import MeasurementReport
import threading

import time
from utils.rsrq import rsrq
from msg.RRCConnectionControlMsg import RRCConnectionControlMsg
from msg.Msg import Msg
from classes.Node import Node

class UE(Node):
    def __init__(self, *args):
        super(UE, self).__init__(*args)
        self.connectedENB=None
        self.handoverENB=None
        self.type="UE"


    def checkA3(self,params):
        while(self.connectedENB != None):
            servingSS = rsrq(self.pos(),self.connectedENB.pos())
            for e in params.enbsToMeasure:
                nSS=rsrq(self.pos(),e.pos())
                if nSS > servingSS + params.threshold + params.hysteresis + params.offset:
                    print("A3 Event Triggered, going to wait for "+str(params.reportTime)+" secs.")
                    time.sleep(params.reportTime)
                    servingSS = rsrq(self.pos(),self.connectedENB.pos())
                    nSS=rsrq(self.pos(),e.pos())
                    if nSS > servingSS + params.threshold + params.hysteresis + params.offset:
                        print("A3 Event Confirmed.. Sending Response Back")
                        self.send(Msg("RRCMeasurementResponse",MeasurementReport(e),self,self.connectedENB), True)
                        time.sleep(10)
                    else:
                        print("A3 Event Failed")

    

    def eventA3(self,params):

        t = threading.Thread(target=self.checkA3, args=[params])
        t.start()
    
    
    def RRCConnectionControl(self,payload:RRCConnectionControlMsg):
        if(payload.eventType=="A3"):
            self.eventA3(payload)


    def parseMsg(self, msg: Msg):
        super().parseMsg(msg)
        if msg.type=="RRCConnectionControlMsg":
            self.RRCConnectionControl(msg.payload)

        if msg.type=="RRCConnectionReconfigurationMsg":
            self.delayedSendCall(Msg("RACHPreambleMsg",None,self,msg.payload.targetENB),True)

        if msg.type == "RACHPreambleACK":
            self.delayedSendCall(Msg("RRCConfigurationComplete",None,self,msg.src), True)