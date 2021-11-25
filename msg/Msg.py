class Msg:
    def __init__(self,type,payload,src,dst) -> None:
        self.type =type
        self.payload=payload
        self.dst=dst
        self.src=src