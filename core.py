###############################################################################
#Informations à propos du projet
###############################################################################
#Document réalisé par :
#    Alexandre Parès
#    Raphaël Guerin
#    
#Dernières version disponible sur le repo Github:
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
graph_fenetre("choix_difficulte")

###############################################################################
#Étape 2 : Creation de la grille + création des cases
###############################################################################
#creation_grille_vide() #Création de la grille
cases(xybombe[0],xybombe[1]) #Remplissage de la grille
 
###############################################################################
#Étape 3 : Remplissage de la grille de bombes + remplissage des cases de chiffre
###############################################################################
bombplace(xybombe) #Placement des bombes
bombchiffre() #Calcul du nombre de bombes autour de chaque cases
###############################################################################
#Étape 4 : Affichage de la grille
###############################################################################

graph_fenetre("grille")

###############################################################################
#Étape 5 : Affichage de la fenetre en fonction du resultat du joueur
###############################################################################
#graph_fenetre("resultat")

###############################################################################
#Test : partie réservée au test
###############################################################################