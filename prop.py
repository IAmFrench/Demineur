###############################################################################
#Informations du module
###############################################################################
#Module prop

###############################################################################
#fonctionnalitées du module du module
###############################################################################
######################
#Variables par défaut#
######################
xgrille=-1
ygrille=-1
grille={}
difficulte=""
nbbombe=-1

#####################
#Couleurs par défaut#
#####################
def difficulte(niveau):    
    ####################################
    #Importation des varialbes globales#
    ####################################

    """
    3 niveaux de difficulté
        "facile" -> 9x9 et 10 bombes
        "intermediaire" -> 16x16 et 20 bombes
        "expert" -> 30x16 et 30 bombes
    """
    if niveau=='facile':
        xgrille=9
        ygrille=9
        nbbombe=10
        xybombe=[9,9,10]
        print('9x9 et 10 bombes')
    elif niveau=='intermediaire':
        xgrille=16
        ygrille=16
        nbbombe=40
        xybombe=[16,16,40]
        print('16x16 et 20 bombes')
    elif niveau=='expert':
        xgrille=30
        ygrille=16
        nbbombe=99
        xybombe=[30,16,99]
        print('30x16 et 30 bombes') 
    else :
        return('Erreur')
    return(xybombe)    
    
     
def couleur(style,r):
    DarkBlue_Red={"r1":"1A2530",
                  "r2":"2C3E50",
                  "r3":"34495E",
                  "r4":"E74C3C",
                  "r5":"FFFFFF",
                  }
    Flat_design_colors={"r1":"334D5C",
                        "r2":"45B29D",
                        "r3":"EFC94C",
                        "r4":"E27A3F",
                        "r5":"DF5A49",
                        }
    defaut={"r1":"113F59",
            "r2":"19BEC0",
            "r3":"20D6C7",
            "r4":"F3EDD3",
            "r5":"D54F58",            
            }
    if style==DarkBlue_Red:
        return(DarkBlue_Red[r])
    else:
        return("#"+defaut[r])