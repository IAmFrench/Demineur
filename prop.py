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
statut_plein_ecran=[False] #Plein ecran désactivé par défaut
mode_presentation=False #Active le mode de présentation
#####################
#Couleurs par défaut#
#####################
#A savoir sur les niveau de couleur
#le niveau "standard" est r3, exemple la grille viens d'être crée
#lorsqu'une case est cliqué, la couleur change pour devenir "active"
#On utilise donc le niveau r2
#Etc...
#Voir les palettes sur https://color.adobe.com/
def couleur(style,r):
    """ Contient les palettes de couleur """
    DarkBlue_Red={"r1":"1A2530", #bordures
                  "r2":"2C3E50", #Case par défaut
                  "r3":"34495E", #Bombe
                  "r4":"E74C3C", #Case visible
                  "r5":"FFFFFF", #Drapeau
                  }
    Flat_design_colors={"r1":"334D5C",
                        "r2":"45B29D",
                        "r3":"EFC94C",
                        "r4":"E27A3F",
                        "r5":"DF5A49",
                        }
    defaut={"r1":"1A2732", #Voir sur https://color.adobe.com/fr/Sytherworks-2014-color-theme-3711492/
            "r2":"51626F",
            "r3":"D3222A",
            "r4":"DFE5E6",
            "r5":"4ECCC3",            
            }
    if style==DarkBlue_Red:
        return("#"+DarkBlue_Red[r])
    else:
        return("#"+defaut[r])

def couleur_chiffre(chiffre):
    """ contient les code hexa de chaque niveau de couleur pour les chiffres """
    dico_couleur={"1":"#414FBD", #bleu clair
                  "2":"#216700", #vert foncé
                  "3":"#AD0501", #rouge clair
                  "4":"#020084", #vrai démineur (bleu foncé)
                  "5":"#83181A", #rouge
                  "6":"#037882", #ciant
                  "7":"#AF0606", #rouge
                  "8":"#AD040D"} #rouge foncé
    return(dico_couleur[chiffre])