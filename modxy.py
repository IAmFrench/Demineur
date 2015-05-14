
from math import *

def coord(x,y,difficulty):
    if difficulty=="facile":
        x=ceil(x/40)
        y=ceil(y/40)
        print(x)
        print(y)
        xy=str(x)+"x"+str(y) #la clé de la case :) 
        


coord(42,120,"facile")
    