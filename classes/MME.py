from classes.Node import Node
from utils.colors import YELLOW


class MME(Node):
    def __init__(self, *args):
        super(MME, self).__init__(*args)
        self.connectedENBs=[]
        self.color=(102,0,52)
        self.type="MME"

    def addENB(self,enb):
        self.connectedENBs.append(enb)


    def display(self):
        super().display()
        for e in self.connectedENBs:
            self.pygame.draw.line(self.screen,(102,0,52),self.pos(),e.pos(),2)
