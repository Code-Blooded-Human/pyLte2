class Msg:
    def __init__(self,type,payload,src,dst,fail=False) -> None:
        self.type =type
        self.payload=payload
        self.dst=dst
        self.src=src
        self.fail=fail