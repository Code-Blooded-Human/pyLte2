from classes.MME import MME
from msg.RRCConnectionControlMsg import RRCConnectionControlMsg
from utils.util import connectUEAndEND
from classes.ENB import ENB
from msg.Msg import Msg
from pygame import time
from classes.Node import Node
from classes.UE import UE
from utils.colors import *
import pygame
import threading
import time

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
FPS=30



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LTE Handover Triggering Simulation")

ue = UE(pygame,screen,100,100,"UE")
enbs = [ENB(pygame,screen,150,150,"ENB0"),ENB(pygame,screen,250,150,"ENB1")]

mme = MME(pygame,screen,250,250,"MME")

for e in enbs:
    e.ue=ue
    mme.addENB(e)
    e.mme=mme


connectUEAndEND(ue,enbs[0])
nodes =[ue,*enbs, mme]

def background():
    time.sleep(5)
    enbs[0].send(Msg("RRCConnectionControlMsg",RRCConnectionControlMsg(enbs,"A3",0,0,0),enbs[0],ue),True)
    pass

t=threading.Thread(target=background)
t.start()


clock = pygame.time.Clock()
running = True
while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(0,len(nodes)):            
                    if nodes[i].shape.collidepoint(event.pos):
                        nodes[i].isDragging= True
                        mouse_x, mouse_y = event.pos
                        offset_x = nodes[i].shape.x - mouse_x
                        offset_y = nodes[i].shape.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for i in range(0,len(nodes)):
                    nodes[i].isDragging=False            
    

        elif event.type == pygame.MOUSEMOTION:
            for i in range(0,len(nodes)):
                if nodes[i].isDragging:
                    mouse_x, mouse_y = event.pos
                    nodes[i].shape.x = mouse_x + offset_x
                    nodes[i].shape.y = mouse_y + offset_y

    screen.fill(WHITE)

    t=pygame.time.get_ticks()

    font=pygame.font.Font(None,20)
    scoretext=font.render(str(t/1000), 1,(0,0,0))
    screen.blit(scoretext, (10,10))


    for i in range(0,len(nodes)):
        nodes[i].display()

    pygame.display.flip()


    clock.tick(FPS)



pygame.quit()