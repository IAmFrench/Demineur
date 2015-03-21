"""
Module Cases
Objectif : créer les différentes
cases en fonction des propriétés
de la grille (taille)
"""
from modgrille import * #besoin du dico grille+tailles
from prop import *
"""
documentation :
grille {'1x1' : [1,2,5,7]
0-1=bombe ou non
2-3=drapeau ou non
4-5=? ou non
6-7=dévoilé ou non
dans ce cas ci, la case
1x1 n'as pas de bombe, a un drapeau, 
pas de ? et n'est pas dévoilé.
"""
def cases(xgrille,ygrille):
    """ Fonction qui crée de la grille """
    for x in range(1,xgrille+1) :
        for y in range(1,ygrille+1) :
            ncase=str(x)+'x'+str(y) #entièrement inutile, juste pour ahérer le code
            grille[ncase]=[1,3,5,7]#ni bombe,ni drapeau, ni ? et ni dévoilée


"""
normalement à ce stade la grille est pleine de cases
resultat du dictionnaire grille :

grille={'1x1' = [1,3,5,7],
        '1x2' = [1,3,5,7],
         ...
        }
"""

def gr(xygrille,prop,statut):
    """
    liste des diff. prop :
        -all
        -bombe
        -drapeau
        -interrogation
        -visible    
    """
    cle=xygrille
    for cle in grille.keys():
    
    
    
"""
Usage de la fonction gr()

exemple 1 :
        gr(1x1,drapeau,true)
    résultat :
        la case de coordonnée 1par1 a un drapeau, donc 3 passe à 2

exemple2:
        (on admet que la case 1x1 a une bombe)
        gr(1x1,bombe,statut)
    résultat :
        retourne la valeur True

exemple3:
        gr(1x1,)
        
"""