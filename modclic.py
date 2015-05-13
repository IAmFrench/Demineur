##############################################################################
#Module permettant que lorsqu'on clic sur une case qui n'est ni une bombe ni un chiffre
#les cases adjacentes soient découverte à leur tour, si l'une d'elles ne contient ni bombe 
#ni chiffre alors les cases qui lui sont adjacentes seront découverte à leur tour ect.
###############################################################################

from prop import *
from modgrille import *
from modcases import *
from modbombe import *
from modgraph import *

def boucle(casereg):
    dec=grille[casereg]
    dec[3]=6
    if dec[4]==-1:
        clic0(casereg)


def clic0(caseclic):
    if len(caseclic)==3:
        x=int(caseclic[0])   
        y=int(caseclic[2])
    if len(caseclic)==5:
        x=int(caseclic[0]+caseclic[1])  
        y=int(caseclic[3]+caseclic[4]) 
    print(x)
    print(y)

    case=grille[caseclic]
    if case[3]==6:
        return(0)
        
    elif case[4]==-1:        
        casereg=str(x-1)+"x"+str(y)
        if x-1!=0:
            boucle(casereg)
       
        casereg=str(x+1)+"x"+str(y) 
        if x+1!=(int(xgrille)+1):
            boucle(casereg)    
           
        casereg=str(x)+"x"+str(y+1) 
        if y+1!=(int(xgrille)+1):
            boucle(casereg)    
          
        casereg=str(x)+"x"+str(y-1) 
        if y-1!=0:
            boucle(casereg)    
            
        casereg=str(x-1)+"x"+str(y-1) 
        if y-1!=0 and x-1!=0:
            boucle(casereg)    
        
        casereg=str(x+1)+"x"+str(y+1) 
        if y+1!=(int(ygrille)+1) and x+1!=(int(xgrille)+1):
            boucle(casereg)    
          
        casereg=str(x+1)+"x"+str(y-1) 
        if y-1!=0 and x+1!=(int(xgrille)+1):
            boucle(casereg)
               
        casereg=str(x-1)+"x"+str(y+1) 
        if y+1!=(int(ygrille)+1) and x-1!=0:
            boucle(casereg)
        
    
graph_fenetre("choix_difficulte")
cases(xybombe[0],xybombe[1])  
bombplace(xybombe)
bombchiffre() 
    
clic0("5x5")    