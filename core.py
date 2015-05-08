"""
Document réalisé par :
    Alexandre Parès
    Raphaël Guerin
    Alexandre Quintais
    
Dernières version disponible sur le repo Github:
https://github.com/IAmFrench/Demineur

sous Licence CC BY-NC-ND 3.0:
https://creativecommons.org/licenses/by-nc-nd/3.0

->Attribution
->Pas d'Utilisation Commerciale  
->Pas de modifications
"""
from modgrille import *
from modcases import *
from prop import *
from modbombe import *
"""
Étape 1 : Creation de la grille + création des cases
"""
cases(xgrille,ygrille)
 

"""
Étape 2 : Remplissage de la grille de bombes + remplissage des cases de chiffre
"""

bombplace()
bombchiffre()

"""
Test : partie réservée au test
"""