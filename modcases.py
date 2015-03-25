"""
Module Cases
Objectif : créer les différentes
cases en fonction des propriétés
de la grille (taille)
Usage dictionnaire :
http://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2

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
    Rappel (o=oui/n=non):
        obombe=0
        nbombe=1
        odrapeau=2
        ndrapeau=3
        ointerro=4
        ninterro=5
        ovisible=6
        nvisible=7
    """
        
    for cle, definition in grille.keys(): #parcours a la fois les clef et leur definition
        if xygrille==cle: #lorsque la clé correspond
            
            """
            Renvoi un oui/non selon la propriété
            """
            if statut=='statut':
                if prop=='bombe':
                    if 0 in definition:
                         rbombe=True
                         return(rbombe)
                    else :
                        rbombe=False
                        return(rbombe)
                        
                elif prop=='drapeau':
                    if 2 in definition:
                        rdrapeau=True
                        return(rdrapeau)
                    else :
                        rdrapeau=False
                        return(rdrapeau)
                        
                elif prop=='interrogation':
                    if 4 in definition:
                        rinterro=True
                        return(rinterro)
                    else:
                        rinterro=False
                        return(rinterro)
                        
                elif prop=='visible':
                    if 6 in definition:
                        rvisible=True
                        return(rvisible)
                    else:
                        rvisible=False
                        return(rvisible)

            """
            Modifie les propriété
            """
            if statut==True or statut==False:
                for a in definition :
                    """
                    Passe de non vers oui
                    """
                    if statut==True:
                        propriete=definition
                        if prop=='bombe':
                            if a==1:
                                propriete[0]=0
                        elif prop=='drapeau':
                            if a==3:
                                propriete[1]=2
                        elif prop=='interrogation':
                            if a==5:
                                propriete[2]=4
                        elif prop=='visible':
                            if a==7:
                                propriete[3]=6
                    """
                    Passe de oui vers non
                    """
                    if statut==False:
                        propriete=definition
                        if prop=='bombe':
                            if a==0:
                                propriete[0]=1
                        elif prop=='drapeau':
                            if a==2:
                                propriete[1]=3
                        elif prop=='interrogation':
                            if a==4:
                                propriete[2]=5
                        elif prop=='visible':
                            if a==6:
                                propriete[3]=7
                grille[xygrille]=propriete#met à jours la définition de la clef
        
"""
Usage de la fonction gr()

exemple 1 :
        gr('1x1','drapeau',True)
    résultat :
        la case de coordonnée 1par1 a un drapeau, donc 3 passe à 2

exemple2:
        (on admet que la case 1x1 a une bombe)
        gr('1x1','bombe','statut')
    résultat :
        retourne la valeur True

exemple3:
        gr('1x1')
        
"""