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
        msg.dst.receive(msg)
        if draw:
            self.transmissions.append(msg)
            t=threading.Thread(target=self.removeMsg, args=[msg])
            t.start()

    def display(self):
        
        #Display the node
        self.pygame.draw.rect(self.screen, self.color, self.shape)
        for t in self.transmissions:
            drawTransmisssionLine(self.pygame,self.screen,BLUE,t.src.pos(),t.dst.pos(),t.type)
        


