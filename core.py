"""
Document réalisé par :
    Alexandre Parès
    Raphaël Guerin
    Alexandre Quintais

Modules :
    propriétés (fn 
    grille (définition de la grille)
    cases (définition des propriétés des cases)
    bombe (insère les bombes aléatoirement ds la grille)
    validateur (valide l'intégrité de la grille et des cases et de leurs propriétés) (optionnel)
    graphique (affichage)
    
    
    
"""
from modgrille import *
from modcases import *
from prop import *

"""
Création de la grille avec les cases + propriétés par défault
"""
cases(xgrille,ygrille)#on applique la fonction

print(grille['1x1'])
gr('1x1','bombe',True)
print(grille['1x1'])