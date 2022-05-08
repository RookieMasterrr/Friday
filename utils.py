def distance(pos1_x,pos1_y,pos2_x,pos2_y)->str:
    w=abs(pos1_x-pos2_x)
    h=abs(pos1_y-pos2_y)
    dis = (w**2+h**2)**0.5
    return str(int(dis))
