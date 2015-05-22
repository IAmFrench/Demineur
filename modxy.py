
from prop import *
from modcases import *
from modbombe import *
from modgraph import *
from modclic import *

graph_fenetre("choix_difficulte")
cases(xybombe[0],xybombe[1])
bombplace(xybombe) 
bombchiffre()



def decouvre():
    for cle in grille:
        case=grille[cle]
        if case[3]==6:
            case_visuel(cle)
       











decouvre()