##############################################################################
#Module permettant que lorsqu'on clic sur une case qui n'est ni une bombe ni un chiffre
#les cases adjacentes soient découverte à leur tour, si l'une d'elles ne contient ni bombe 
#ni chiffre alors les cases qui lui sont adjacentes seront découverte à leur tour ect.
###############################################################################
from math import *

#`from prop import *
#from modcases import *
#from modbombe import *
from modgraph import *
#from modgraph import case_dec (déjà importé a la ligne précédente)
camo=["-1x-1"] #Liste des cases qui ont été modifiées par une action de l'utilisateur


def coord(x,y,difficulty):
   """
   Coord est une fonction qui permet de convertir les coordonnées en pixels d'un 
   clic en coordonnées de la case sur laquelle on à cliqué.
   x: coordonnées x en pixels du clic sur le canvas
   y: coordonnées y en pixels du clic sur le canvas
   difficulty: difficulté, nécessaire pour diviser le nombre de pixels correctement 
   """
   
   
   if difficulty=="facile":
        x=ceil(x/40) #divise le nombre de pixel par le nombre de pixel d'une case.
        y=ceil(y/40)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case 
    
   if difficulty=="intermediaire":
        x=ceil(x/35)
        y=ceil(y/35)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case

   if difficulty=="expert":
        x=ceil(x/25)
        y=ceil(y/25)
        #print(x)
        #print(y)
        xy=str(x)+"x"+str(y) #la clé de la case  

   return(xy)
    

def boucle(casereg): #appelé dans clic0
    """
    Cette fonction permet de découvrir les cases adjacentes à des cases dont la 
    propriété chiffre est égale à -1 (ce qui correspond à une case sans bombe,
    ni drapeau, ni chiffre...) si cette case est aussi un chiffre égale à -1,
    alors elle va appelé clic0.
    casereg: clé d'une case adjacente à une case vide et découverte.
    """
    dec=grille[casereg]
    dec[3]=6
    camo.append(casereg) #ajoute casereg à la liste camo, la liste des cases découvertes lors d'un clic
    if dec[4]==-1: #si la case est un 0 alors on exécute de nouveau clic0 pour découvrir les cases adjacente
        
        clic0(casereg)

def ext_xy(caseclic,XouY):
    """"
    ext_xy est une fonction qui permet d'extraire de la chaine de caractère du
    nom d'une clé (de la bibliothèque grille) le x et le y.
    Par exemple pour caseclic="1x14" elle va renvoyer x=1 et y=14.
    caseclic: le nom de la clé 
    XouY: l'information que l'on souhaite extraire (soit x, soit y)
    """
    if len(caseclic)==3: #extrait x y de la clé si x et y sont inférieur à 10
        x=int(caseclic[0])   
        y=int(caseclic[2])
    if len(caseclic)==5: #extrait x y de la clé si x et y sont supérieur à 10
        x=int(caseclic[0]+caseclic[1])  
        y=int(caseclic[3]+caseclic[4]) 
    if len(caseclic)==4: #extrait x y 
        if caseclic[1]=='x': #extrait x y de la clé si x<10 et y>=10
            x=int(caseclic[0])
            y=int(caseclic[2]+caseclic[3])
        elif caseclic[2]=='x': #extrait x y de la clé si x>=10 et y<10
            x=int(caseclic[0]+caseclic[1])
            y=int(caseclic[3])   
    if XouY=="x":
        return(x)
    elif XouY=="y":
        return(y)
    

def clic0(caseclic):
    """
    clic0 est une fonction qui modifie les propriétés d'une case sur laquelle
    on fait un clic gauche ou qui est à côté d'une case vide qui vient d'être 
    découverte.
    clic0 va vérifier si la case n'a pas un drapeau dans quel cas elle ne fera 
    rien, sinon elle découvrir la case, puis si elle est vide (ni bombe, ni 
    chiffre) elle va découvrir les cases adjacentes en appellant la fonction 
     boucle. Si une de c'est case adjacente est vide boucle va appellé clic0.
    caseclic: clé de la case dont on souhaite modifier les propriétées
    """    
    
    from modgraph import liste_cases_visibles

    case=grille[caseclic]
    if case[1]==2: #vérifie qu'il n'y a pas de drapeau
        return()
        
    case[3]=6 #rend la case visible
    print("case "+caseclic+" est découverte")

    #ajout de la case découverte à la liste des cases découverte (liste_cases_visibles)    
    if caseclic in liste_cases_visibles :#on vérifie que la case n'est pas déja dans la liste
        remarque=""
    else: #si n'est pas dans la liste
        liste_cases_visibles.append(caseclic)
    
    x=ext_xy(caseclic,"x") #on à besoin de connaitre la valeur X et Y des coordonnés
    y=ext_xy(caseclic,'y') #de la case sur la grille, on les extraits donc de la clé
    # x et y font nous permettrent de calculer les coordonnées des cases adjacentes.

    xgrille=xybombe[0] #on extrait de la liste xybombe la longueur et la largeur de la grille
    ygrille=xybombe[1]

    if case[4]==-1:  #si la case est un 0 on va regarder toutes les cases autours pour les découvrirs
        
        casereg=str(x-1)+"x"+str(y) # coordonnées de la case à droite
        if x-1!=0:                  #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:  #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
       
        casereg=str(x+1)+"x"+str(y) # coordonnées de la case à gauche
        if x+1!=(int(xgrille)+1):  #on vérifie avec ce texte que cette case existe 
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
        
        
        casereg=str(x)+"x"+str(y+1) # coordonnées de la case au dessous
        if y+1!=(int(ygrille)+1):   #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
              
          
        casereg=str(x)+"x"+str(y-1) # coordonnées de la case au dessus
        if y-1!=0:      #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
            
        casereg=str(x-1)+"x"+str(y-1) # coordonnées de la case en haut à gauche
        if y-1!=0 and x-1!=0:   #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
        
        casereg=str(x+1)+"x"+str(y+1) # coordonnées de la case en bas à droite
        if y+1!=(int(ygrille)+1) and x+1!=(int(xgrille)+1): #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
          
        casereg=str(x+1)+"x"+str(y-1) # coordonnées de la case en haut à doite
        if y-1!=0 and x+1!=(int(xgrille)+1):    #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:  #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie            
               boucle(casereg)
               
        casereg=str(x-1)+"x"+str(y+1) # coordonnées de la case en bas à gauche
        if y+1!=(int(ygrille)+1) and x-1!=0:    #on vérifie avec ce texte que cette case existe
           visi=grille[casereg]
           if visi[3]!=6:   #on vérifie que la case n'est pas déjà découverte pour éviter de créer une boucle infinie
               boucle(casereg)
               
def clic1(caseclic): #clic droit
    """
    clic1 est une fonction qui modifie les propriétés d'une case lors d'un clic
    droit de souris.
    caseclic: clé de la case sur laquelle on a fait un clic droit
    """
    case=grille[caseclic]
    if case[3]==6: #si la case est découverte on  ne change aucune propriété
        return()
    
    if case[2]==4: #si il y a un ? sur la case
        case[2]=5 #on l'enléve (la case est donc à son statue d'origine)
        print("il n'y plus rien sur la case")
    elif case[1]==2: #si il y a un drapeau sur la case
        case[2]=4   #on l'enléve 
        case[1]=3  #puis on met un ?
        print("il y a un ? sur la case")
    elif case[1]==3: #si il n'y a pas de drapeau sur la case
        case[1]=2   #on en met 1
        print("il y a un drapeau sur la case")
        

