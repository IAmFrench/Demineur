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
#difficulte=""
nbbombe=-1
xybombe=[]

#####################
#Couleurs par défaut#
#####################    
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