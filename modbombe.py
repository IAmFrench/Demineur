from prop import *
import random
from modcases import *
from modgrille import*

cases(xgrille,ygrille)

def bombplace():
    
    nbbombe=int(input("Entrez le nombre de bombe: "))
    for x in range(nbbombe):
        al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))
        while gr(al,'bombe','statut')==True:
            al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))
        gr(al,'bombe',True)
    
#bombplace()
#print(grille)    

