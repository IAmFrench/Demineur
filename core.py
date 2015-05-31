###############################################################################
#Informations à propos du projet
###############################################################################
#Document réalisé par :
#    Alexandre Parès
#    Raphaël Guerin
#    Alexandre Quintais
#
#Dernière version disponible sur le repo Github:
#https://github.com/IAmFrench/Demineur
#
#sous Licence CC BY-NC-ND 3.0:
#https://creativecommons.org/licenses/by-nc-nd/3.0
#
#->Attribution
#->Pas d'Utilisation Commerciale  
#->Pas de modifications

###############################################################################
#Importation des modules
###############################################################################
from prop import *
from modcases import *
from modbombe import *
from modgraph import *
from modclic import *

###############################################################################
#Étape 1 : Affichage fenetre choix
###############################################################################
graph_fenetre("choix_difficulte") #Ouverture fenetre graphique

###############################################################################
#Étape 2 : Creation de la grille + création des cases
###############################################################################
if xybombe[0]!=0: #évite de générer des erreurs si le programme est fermé
    cases(xybombe[0],xybombe[1]) #Remplissage de la grille en fonction du nombre de case horizontale: (xybombe[0]) et verticale:(xybombe[1])
 
###############################################################################
#Étape 3 : Remplissage de la grille de bombes + remplissage des cases de chiffre
###############################################################################
if xybombe[0]!=0:
    bombplace(xybombe) #Placement des bombes
    bombchiffre() #Calcul du nombre de bombes autour de chaque cases

###############################################################################
#Étape 4 : Affichage de la grille
###############################################################################
if xybombe[0]!=0:
    graph_fenetre("grille") #ouverture fenetre graphique

###############################################################################
#Étape 5 : Affichage de la fenetre en fonction du resultat du joueur
###############################################################################
#graph_fenetre("resultat")

###############################################################################
#Test : partie réservée au test
###############################################################################
