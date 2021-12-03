def connectUEAndEND(ue,enb):
    if ue.connectedENB:
        ue.connectedENB.connectedUE=None
    ue.connectedENB=enb
    enb.connectedUE=ue