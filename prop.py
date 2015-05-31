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
    #Bordure, case par défaut, Bombe, Case visible, Drapeau
    keys=["r1","r2","r3","r4","r5"]
    DarkBlue_Red=["1A2530","2C3E50","E74C3C","597DA1","E2FFB2"] #https://color.adobe.com/fr/DarkBlue-Red-color-theme-4053531/
    Flat_design_colors=["334D5C","EFC94C","DF5A49","E27A3F","45B29D"] #https://color.adobe.com/fr/Copie-de-Flat-design-colors-1-color-theme-4079805/
    Ice_Cream=["113F59","19BEC0","D54F58","159FA1","F3EDD3"] #https://color.adobe.com/fr/Ice-Cream-color-theme-4185778
    Alaska_sunset=["BF4E6C","F2676B","F5CC70","5992C7","325982"] #https://color.adobe.com/fr/Alaska-sunset-color-theme-3121915
    Flood=["005572","006573","F4D4AD","81BEAA","008B8D"] #https://color.adobe.com/fr/Flood-color-theme-4203435/
    dico={}
    styles={"nom a afficher":"nom variable",
            "DarkBlue Red":"DarkBlue_Red",
            "Flat design":"Flat_design_colors",
            "Ice Cream":"Ice_Cream",
            "Alaska sunset":"Alaska_sunset",
            "Flood":"Flood"}
            
    style=styles[style] #Cherche le nom de la variable
    r=keys.index(r) #prend la position de l'élément
    
    if style=="DarkBlue_Red":
        resultat=DarkBlue_Red[r]
    elif style=="Flat_design_colors":
        resultat=Flat_design_colors[r]
    elif style=="Ice_Cream":
        resultat=Ice_Cream[r]
    elif style=="Alaska_sunset":
        resultat=Alaska_sunset[r]
    elif style=="Flood":
        resultat=Flood[r]
    else :
        return("ERROR")
    return("#"+resultat)

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