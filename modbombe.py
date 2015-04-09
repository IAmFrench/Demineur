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

def num():
    if gr(grillereg,'bombe','statut')==True:
        gr(xyg,'chiffre',(gr(xyg,'chiffre',statut)+1))
        
        

def bombchiffre():
    for i in range(0;int(xgrille*ygrille)): 
        
        xyg=str(x)+x+str(y)
        grillereg=str(xgrille-1)+x+str(ygrille)
        if grillereg!=0:
           num()
        
        grillereg=str(xgrille+1)+x+str(ygrille)
    
