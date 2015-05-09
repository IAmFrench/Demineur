###############################################################################
#Informations du module
###############################################################################
#Module Cases
#Usage dictionnaire :
#http://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2
#Explication détaillé du modulen :
#https://github.com/IAmFrench/Demineur/wiki/Fonction-modcases

###############################################################################
#Importation des modules
###############################################################################
from modgrille import * #besoin du dico grille+tailles
from prop import *

###############################################################################
#fonctionnalitées du module du module
###############################################################################
def cases(xgrille,ygrille):
    """ Fonction qui créé les cases dans la grille """
    for x in range(1,xgrille+1) :
        for y in range(1,ygrille+1) :
            ncase=str(x)+'x'+str(y) #entièrement inutile, juste pour ahérer le code
            grille[ncase]=[1,3,5,7,-1]#ni bombe,ni drapeau, ni ? et ni dévoilée

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
            if definition[1]==2:
                rdrapeau=True
                return(rdrapeau)
            
            elif definition[1]==3 :
                rdrapeau=False
                return(rdrapeau)
            else:
                print("ERREUR->Case_statut "+prop+" "+xygrille)
                
        elif prop=='interrogation':
            if definition[2]==4:
                rinterro=True
                return(rinterro)
            elif definition[2]==5:
                rinterro=False
                return(rinterro)
            else :
                print("ERREUR->Case_statut "+prop+" "+xygrille)
                
        elif prop=='visible':
            if definition[3]==6:
                rvisible=True
                return(rvisible)
            elif definition[3]==7:
                rvisible=False
                return(rvisible)
            else :
                print("ERREUR->Case_statut "+prop+" "+xygrille)
        elif prop=='chiffre':
            return(definition[4]) #ENTIER
    
    
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
        """  la valeur du nombre de bombe """
        definition[4]=int(statut)
        
    ##################
    ###Test logique###
    ##################
    
    if statut=='statut':
        return(case_statut())
        ###
        #print("Statut='statut'")
        ###
        
    if type(statut)==bool: #Statut = true ou Flase
        if statut==True :#On demande a activer la propriété
            return(case_offon())
        ###
        #print("statut=True")
        ###
    
        if statut==False: #On demande a désactiver la propriété
            return(case_onoff())
            ###
            #print("Statut=False")
            ###
    if statut !=bool and type(statut)==int and prop=='chiffre' : #satut == un entier différent de booleen
        return(case_nbbombe())
        ###
        #print("Statut=chiffre")
        ###

###############################################################################
#Exemple d'utilisation
###############################################################################
#Usage de la fonction gr()
#exemple 1 :
#        gr('1x1','drapeau',True)
#    résultat :
#        la case de coordonnée 1par1 a un drapeau, donc 3 passe à 2
#exemple2:
#        (on admet que la case 1x1 a une bombe)
#        gr('1x1','bombe','statut')
#    résultat :
#        retourne la valeur True
#exemple3:
#        gr('1x1','chiffre,'1')
#   résultat:
#       il y a 1 bombe a coté de la case