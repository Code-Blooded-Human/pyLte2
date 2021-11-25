import math

def rsrq(src,dst):
    x=(src[0]-dst[0])**2
    y=(src[1]-dst[1])**2
    xy=math.sqrt(x+y)
    return round(1/xy*100,3)