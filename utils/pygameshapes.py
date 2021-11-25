from utils.colors import *
import math

def drawTransmisssionLine(pygameinstance, screen, color, startp, endp, label, labelColor=BLACK):
        draw_arrow(pygameinstance,screen, color ,startp, endp)
        font=pygameinstance.font.Font(None,20)
        scoretext=font.render(label, 1,labelColor)
        screen.blit(scoretext, ((startp[0]+endp[0])/2,(startp[1]+endp[1])/2))

def draw_arrow(pygameinstance,screen, color, start, endp):
    ratio=3
    end=[1,2]
    end[0]=(endp[0]*ratio+start[0])/(ratio+1)
    end[1]=(endp[1]*ratio+start[1])/(ratio+1)
    pygameinstance.draw.line(screen,color,start,end,2)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    scale=10
    pygameinstance.draw.polygon(screen, color, ((end[0]+scale*math.sin(math.radians(rotation)), end[1]+scale*math.cos(math.radians(rotation))), (end[0]+scale*math.sin(math.radians(rotation-120)), end[1]+scale*math.cos(math.radians(rotation-120))), (end[0]+scale*math.sin(math.radians(rotation+120)), end[1]+scale*math.cos(math.radians(rotation+120)))))
