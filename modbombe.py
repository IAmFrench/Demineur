from prop import *
import random
from modcases import *
from modgrille import*



def bombplace():
    
    nbbombe=int(input("Entrez le nombre de bombe: "))
    for x in range(nbbombe):
        al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))
        while gr(al,'bombe','statut')==False:
            al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))
        gr(al,'bombe',True)
    

    

def num(grillereg,xyg):
    if gr(xyg,'bombe','statut')==True:
        #print(int(gr(grillereg,'chiffre','statut')+1))
        gr(grillereg,'chiffre',int(gr(grillereg,'chiffre','statut')+1))
        

def bombchiffre():
    for x in range(1,int(xgrille)):
        for y in range(1,int(ygrille)):
            xyg=str(x)+"x"+str(y)
            
            grillereg=str(x-1)+"x"+str(y)
            if x-1!=0:
                num(grillereg,xyg)
        
            grillereg=str(x+1)+"x"+str(y)
            if x+1!=(int(xgrille)+1):
                num(grillereg,xyg)
                
            grillereg=str(x)+"x"+str(y+1)
            if y+1!=(int(xgrille)+1):
                num(grillereg,xyg)
            
            grillereg=str(x)+"x"+str(y-1)
            if y-1!=0:
                num(grillereg,xyg)
            
            grillereg=str(x-1)+"x"+str(y-1)
            if y-1!=0 and x-1!=0:
                num(grillereg,xyg)
            
            grillereg=str(x+1)+"x"+str(y+1)
            if y+1!=(int(ygrille)+1) and x+1!=(int(xgrille)+1):
                num(grillereg,xyg)
            
            grillereg=str(x+1)+"x"+str(y-1)
            if y-1!=0 and x+1!=(int(xgrille)+1):
                num(grillereg,xyg)
                
            grillereg=str(x-1)+"x"+str(y+1)
            if y+1!=(int(ygrille)+1) and x-1!=0:
                num(grillereg,xyg)
    
            
    #return(grille)



