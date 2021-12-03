from utils.pygameshapes import drawTransmisssionLine
from utils.colors import *
from utils.rsrq import rsrq
from msg.Msg import Msg
import threading
import time


class Node:
    def __init__(self,pygame,screen,x,y,name):
        
        self.name = name;
        
        self.isDragging=False
        self.shape= pygame.rect.Rect(x, y, 17, 17)
        self.pygame= pygame
        self.color= RED
        self.screen = screen;
        self.type=None
        self.transmissions = [];

    def pos(self):
        return (self.shape.x,self.shape.y)

    def parseMsg(self,msg:Msg):
        pass
    
    def receive(self,msg:Msg):
        self.parseMsg(msg)

    def removeMsg(self, msg):
        time.sleep(2)
        self.transmissions.remove(msg)
    
    def sendDelay(self,*args):
        time.sleep(2)
        self.send(*args)
    
    def delayedSendCall(self,*args):
        t=threading.Thread(target=self.sendDelay, args=[*args])
        t.start()
        pass
    
    
    def send(self,msg:Msg,draw=False):

        # Simulation : The msg must fail if signal is weaker than 0.2
        if rsrq(msg.dst.pos(),msg.src.pos()) < 0.5 and ( (msg.src.type == "UE" or msg.dst.type=="UE") ):
            print("Message sending failed")
            msg.fail=True
        else:
            msg.dst.receive(msg)
        
        if draw:
            self.transmissions.append(msg)
            t=threading.Thread(target=self.removeMsg, args=[msg])
            t.start()

    def display(self):
        
        #Display the node
        self.pygame.draw.rect(self.screen, self.color, self.shape)
        for t in self.transmissions:
            color = BLUE
            label = t.type
            if t.fail == True:
                color = RED
                label = t.type +" FAILED X"
            drawTransmisssionLine(self.pygame,self.screen,color,t.src.pos(),t.dst.pos(),label)
        


