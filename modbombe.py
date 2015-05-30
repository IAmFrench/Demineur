###############################################################################
#Informations du module
###############################################################################
#Modbombe

###############################################################################
#Importation des modules
###############################################################################
#from prop import *
import random
from modcases import * # pour la fonction gr()

###############################################################################
#fonctionnalitées du module du module
###############################################################################

def bombplace(xybombe): #appellé dans core
    """xybombe: liste contenant la taille de la grille et le nombre de bombe
    Place les bombes de façon aléatoire dans la bibliothéque"""
    xgrille=xybombe[0] #extraction des différentes données de xybombe
    ygrille=xybombe[1]
    nbbombe=xybombe[2]
    for x in range(nbbombe):
        al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))   #Permet de choisir une clé aléatoire.
        while gr(al,'bombe','statut')==True:
            al=str(random.randint(1,xgrille))+'x'+str(random.randint(1,ygrille))
        gr(al,'bombe',True) #Modifie les propriétés de la clé choisie 
        gr(al,'chiffre',-2) #Modifie les propriétés de la clé choisie
        from modgraph import liste_bombes
        liste_bombes.append(al) #ajoute la clé ou on vient de mettre une bombe à la liste des clé contenant une bombe
    print("Bombes placées")
    
            

def num(grillereg,xyg):  #appellée dans bombchiffre
    """xyg: case dont on vérifie le voisinage pour modifier son chiffre
    grillereg: case voisine dont regarde les propriétés pour voir si on doit ajouter 1 a xyg
    Ajoute 1 à la case xyg si il y a une bombe dans la case grillereg"""
    
   # if gr(grillereg,'bombe','statut')==True:
  #      if gr(xyg,'bombe','statut')==False: 
  #          gr(xyg,'chiffre',int(gr(xyg,'chiffre','statut')+1))
    
    if gr(grillereg,'bombe','statut')==True: #Vérifie si il y a une bombe dans la case grillereg
       if gr(xyg,'bombe','statut')==False:  #Si il y a une bombe dans la case xyg on ne va pas modifier son chiffre
           
           defi=grille[xyg]
           defi[4]=defi[4]+1
       else:
           defi=grille[xyg]
           defi[4]=-2

def bombchiffre(): #appellée dans core
    """Cette fonction va regarder les cases adjacentes à chaques clé"""

    xgrille=xybombe[0]
    ygrille=xybombe[1]
    #nbbombe=xybombe[2]
    for x in range(1,int(xgrille)+1): 
        for y in range(1,int(ygrille)+1):
            xyg=str(x)+"x"+str(y)  #xyg prend les valeurs de toutes les clés de la grille
            grillereg=str(x-1)+"x"+str(y) #grillereg est la case regardé, ici elle prend la valeur de la clé à gauche de xyg
            if x-1!=0:  #vérifie si la clé xyg existe
                num(grillereg,xyg)
        
            grillereg=str(x+1)+"x"+str(y) #case à droite
            if x+1!=(int(xgrille)+1): 
                num(grillereg,xyg)
                
            grillereg=str(x)+"x"+str(y+1) #case du dessous
            if y+1!=(int(ygrille)+1):
                num(grillereg,xyg)
            
            grillereg=str(x)+"x"+str(y-1) #case du dessus
            if y-1!=0:
                num(grillereg,xyg)
            
            grillereg=str(x-1)+"x"+str(y-1) #case à gauche en bas
            if y-1!=0 and x-1!=0:
                num(grillereg,xyg)
            
            grillereg=str(x+1)+"x"+str(y+1) #case à droite en bas
            if y+1!=(int(ygrille)+1) and x+1!=(int(xgrille)+1):
                num(grillereg,xyg)
            
            grillereg=str(x+1)+"x"+str(y-1) #case à doite en haut
            if y-1!=0 and x+1!=(int(xgrille)+1):
                num(grillereg,xyg)
                
            grillereg=str(x-1)+"x"+str(y+1) #case à gauche en haut
            if y+1!=(int(ygrille)+1) and x-1!=0:
                num(grillereg,xyg)
    print('chiffres placés')
            
    #return(grille)
