
from classes.ENB import ENB
from classes.UE import UE


def connectUEAndEND(ue:UE,enb:ENB):
    ue.connectedENB=enb
    enb.connectedUE=ue