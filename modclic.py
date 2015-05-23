##############################################################################
#Module permettant que lorsqu'on clic sur une case qui n'est ni une bombe ni un chiffre
#les cases adjacentes soient découverte à leur tour, si l'une d'elles ne contient ni bombe 
#ni chiffre alors les cases qui lui sont adjacentes seront découverte à leur tour ect.
###############################################################################
from math import *

#`from prop import *
#from modcases import *
#from modbombe import *
from modgraph import *
#from modgraph import case_dec (déjà importé a la ligne précédente)
camo=["-1x-1"] #Liste des cases qui ont été modifiées par une action de l'utilisateur


def coord(x,y,difficulty):
   
   if difficulty=="facile":
        x=ceil(x/40) #divise le nombre de pixel par le nombre de pixel d'une case.
        y=ceil(y/40)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case :) 
    
   if difficulty=="intermediaire":
        x=ceil(x/35)
        y=ceil(y/35)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case :) 

   if difficulty=="expert":
        x=ceil(x/25)
        y=ceil(y/25)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case :) 

   return(xy)
    
def GameOver(): #appelé dans clic0
    print("GAME OVER!!")

def boucle(casereg): #appelé dans clic0

    dec=grille[casereg]
    dec[3]=6
    camo.append(casereg)
    if dec[4]==-1: #si la case est un 0 alors on exécute de nouveau clic0 pour découvrir les cases adjacente
        
        clic0(casereg)

def ext_xy(caseclic,XouY):
    if len(caseclic)==3: #extrait x y de la clé
        x=int(caseclic[0])   
        y=int(caseclic[2])
    if len(caseclic)==5:
        x=int(caseclic[0]+caseclic[1])  
        y=int(caseclic[3]+caseclic[4]) 
    if len(caseclic)==4:
        if caseclic[1]=='x':
            x=int(caseclic[0])
            y=int(caseclic[2]+caseclic[3])
        elif caseclic[2]=='x':
            x=int(caseclic[0]+caseclic[1])
            y=int(caseclic[3])   
    if XouY=="x":
        return(x)
    elif XouY=="y":
        return(y)
    

def clic0(caseclic): #clic gauche
    case=grille[caseclic]

    

    if case[1]==2: #vérifie qu'il n'y a pas de drapeau
        return()
        
    case[3]=6 #rend la case visible
    print("case "+str(caseclic)+" est découverte")
    
    if case[4]==-2: #
        GameOver()
        
    x=ext_xy(caseclic,"x")
    y=ext_xy(caseclic,'y')

    xgrille=xybombe[0]
    ygrille=xybombe[1]

    if case[4]==-1:  #si la case est un 0 on va regarder toutes les cases autours pour les découvrirs
        casereg=str(x-1)+"x"+str(y)
        if x-1!=0:
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
       
        casereg=str(x+1)+"x"+str(y) 
        if x+1!=(int(xgrille)+1):
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
        
        
        casereg=str(x)+"x"+str(y+1) 
        if y+1!=(int(ygrille)+1):
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
              
          
        casereg=str(x)+"x"+str(y-1) 
        if y-1!=0:
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
            
        casereg=str(x-1)+"x"+str(y-1) 
        if y-1!=0 and x-1!=0:
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
        
        casereg=str(x+1)+"x"+str(y+1) 
        if y+1!=(int(ygrille)+1) and x+1!=(int(xgrille)+1):
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
          
        casereg=str(x+1)+"x"+str(y-1) 
        if y-1!=0 and x+1!=(int(xgrille)+1):
           visi=grille[casereg]
           if visi[3]!=6:              
               boucle(casereg)
               
        casereg=str(x-1)+"x"+str(y+1) 
        if y+1!=(int(ygrille)+1) and x-1!=0:
           visi=grille[casereg]
           if visi[3]!=6:
               boucle(casereg)
               
def clic1(caseclic): #clic droit
    case=grille[caseclic]
    if case[3]==6:
        return()
    
    if case[2]==4: #si il y a un ? sur la case
        case[2]=5
        print("il n'y plus rien sur la case")
    elif case[1]==2: #si il y a un drapeau sur la case
        case[2]=4
        case[1]=3
        print("il y a un ? sur la case")
    elif case[1]==3: #si il n'y a pas de drapeau sur la case
        case[1]=2
        print("il y a un drapeau sur la case")
        
"""
graph_fenetre("choix_difficulte")
cases(xybombe[0],xybombe[1])  
bombplace(xybombe)
bombchiffre() 
clic0("9x9")
coord(52,38,"facile")  
print(coord(52,38,"facile")  )
"""