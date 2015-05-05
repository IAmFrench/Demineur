"""
Module Cases
Usage dictionnaire :
http://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2
Explication détaillé de la fonction :
https://github.com/IAmFrench/Demineur/wiki/Fonction-modcases
"""
from modgrille import * #besoin du dico grille+tailles
from prop import *

def cases(xgrille,ygrille):
    """ Fonction qui crée de la grille """
    for x in range(1,xgrille+1) :
        for y in range(1,ygrille+1) :
            ncase=str(x)+'x'+str(y) #entièrement inutile, juste pour ahérer le code
            grille[ncase]=[1,3,5,7,0]#ni bombe,ni drapeau, ni ? et ni dévoilée

"""
>>
    Rappels
>>
"""
"""
liste des diff. prop :
    -bombe
    -drapeau
    -interrogation
    -visible
    -chiffre
Rappel (o=oui/n=non):
    obombe=0
    nbombe=1
    odrapeau=2
    ndrapeau=3
    ointerro=4
    ninterro=5
    ovisible=6
    nvisible=7
Statuts :
    true
    False
    Statut
    (ou chiffre pour chiffre)
"""



"""
>>
    Fonction gr
>>
"""
def gr(xygrille,prop,statut):
    definition=grille[xygrille] #charge les propriété de la clé demandé
    ###################
    ###Les variables###
    ###################
    
    
    ###################
    ###Les Fonctions###
    ###################
    """
    >>
        Affiche le statut d'une case
    >>
    """
    def case_statut():
        """ Affiche le statut (True/False) de la case """
        if prop=='bombe':
            if definition[0]==0:
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
        elif prop=='chiffre':
            return int((definition[4])) #ENTIER
    
    
    """
    >>
        Modifie le statut d'une case (non->oui)
    >>
    """
    def case_offon():
        """ Active la propriété """
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
        grille[xygrille]=propriete #met à jours la définition de la clef

    
    """
    >>
        Modifie le statut d'une case (oui->non)
    >>
    """
    def case_onoff():
        """ Désactive le statut de la propriété """
        """
            Passe de oui vers non
        """
        for a in definition :
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
        grille[xygrille]=propriete #met à jours la définition de la clef
        
    def case_nbbombe():
        """ Renvoi la valeur du nombre de bombe """
        """
        Spécial pour le nombre de bombes
        """
        if statut != bool and type(statut)==int and prop=='chiffre' : #satut == un entier différent de booleen
            definition[4]=int(statut)
        
    ##################
    ###Test logique###
    ##################
    
    if statut=='statut':
        return(case_statut())
        ###
        print("Statut='statut'")
        ###
        
    if statut==True: #On demande a activer la propriété
        return(case_offon())
        ###
        print("statut=True")
        ###
    
    if statut==False: #On demande a désactiver la propriété
        return(case_onoff())
        ###
        print("Statut=False")
        ###


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

