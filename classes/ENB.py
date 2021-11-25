from classes.RRCConnectionReconfigurationMsg import RRCConnectionReconfigurationMsg
import threading
from classes.HORequest import HOAck, HORequest
from msg.Msg import Msg
from utils.rsrq import rsrq
from utils.colors import YELLOW
from classes.Node import Node
import time

class ENB(Node):
    def __init__(self, *args):
        super(ENB, self).__init__(*args)
        self.ue=None
        self.connectedUE=None
        self.color=YELLOW

   

    def parseMsg(self, msg: Msg):
        super().parseMsg(msg)
        
        if msg.type == "RRCMeasurementResponse":
            
            # self.send(Msg("HORequest",HORequest,self,msg.payload.targetENB), True)
            self.delayedSendCall(Msg("HORequest",HORequest,self,msg.payload.targetENB), True)

        if msg.type == "HORequest":
            # self.send(Msg("HORequestACK",HOAck,self,msg.src), True)
            self.delayedSendCall(Msg("HORequestACK",HOAck,self,msg.src), True)

        if msg.type == "HORequestACK":
            # self.send(Msg("HORequestACK",HOAck,self,msg.src), True)
            self.delayedSendCall(Msg("RRCConnectionReconfigurationMsg",RRCConnectionReconfigurationMsg(msg.src),self,self.connectedUE), True)


        if msg.type == "RACHPreambleMsg":
            self.delayedSendCall(Msg("RACHPreambleACK",None,self,msg.src), True)
            
    
    
    def display(self):

        if self.connectedUE != None:
            self.pygame.draw.line(self.screen,YELLOW,self.pos(),self.connectedUE.pos(),2)

        if self.ue != None:
            signal = rsrq(self.pos(),self.ue.pos())
            font=self.pygame.font.Font(None,20)
            scoretext=font.render(self.name+"  "+str(signal), 1,(0,0,0))
            self.screen.blit(scoretext, (self.shape.x-20, self.shape.y-20))
        
        super().display()
        
