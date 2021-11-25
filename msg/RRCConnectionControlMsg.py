class RRCConnectionControlMsg:
    def __init__(self,enbsToMeasure, event, threshold, hysteresis, offset,reportTime=5) -> None:
        self.enbsToMeasure = enbsToMeasure
        self.eventType = event
        self.threshold = threshold
        self.hysteresis=hysteresis
        self.offset = offset
        self.reportTime = reportTime #How much time to wait before reporting