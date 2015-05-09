###############################################################################
#Informations du module
###############################################################################
#Module graphique
#Objectif : créations des interfaces du programme, interraction avec l'utilisateur


###############################################################################
#Importation des modules
###############################################################################
from tkinter import * #bibliothèque graphique
from prop import * #fonctions pour les propriétés

###############################################################################
#fonctionnalitées du module du module
###############################################################################
"""
>>
    Fonctions Fenêtre (choix_difficulté, grille_demineur, a_propos,etc...)
>>
"""

def graph_fenetre(fonction):
    """
    liste des valeur pour fonction :
    - choix_difficulte
    - grille
    - resultat
    """
    """
    >>
        Creation fenetre choix difficulté
    >>
    """
    def interface_graph_difficulte():
        fenetre_titre="Choix Difficulté"    
        
        fenetre_choix_difficulte = Tk() #création de la fenetre
        
        def difficulte_facile():
            difficulte("facile")
            print("fonction difficulté -> facile")
            fenetre_choix_difficulte.destroy()
            print("fenetre destroy") 
            
        def difficulte_inter():
            difficulte("intermediaire")
            print("fonction difficulté -> inter")
            fenetre_choix_difficulte.destroy()
            print("fenetre destroy")
            
        def difficulte_expert():
            difficulte("expert")
            print("fonction difficulté -> expert")
            fenetre_choix_difficulte.destroy()
            print("fenetre destroy")
    
        fenetre_choix_difficulte.title(fenetre_titre) #titre fenetre
        ########
        #Frames#
        ########
        frame_haut=Frame(fenetre_choix_difficulte)
        #frame_bas=Frame(fenetre_choix_difficulte)
        
        #########
        #Boutons#
        #########
        bouton_facile=Button(frame_haut,text='Facile',width=15,height=3,command=difficulte_facile)
        bouton_facile.pack(side=LEFT,padx=5,pady=5) #alignement à gauche 5px sur les cotés
        
        bouton_intermediaire=Button(frame_haut,text='Intermediaire',width=15,height=3,command=difficulte_inter)
        bouton_intermediaire.pack(side=LEFT,padx=5,pady=5)
        
        bouton_expert=Button(frame_haut,text='Expert',width=15,height=3,command=difficulte_expert)
        bouton_expert.pack(side=LEFT,padx=5,pady=5)
        frame_haut.pack(side=TOP,padx=5, pady=5)
        
        #bouton_suivant=Button(frame_bas,text='Suivant',width=15,height=3,command=fenetre_choix_difficulte.destroy)
        #bouton_suivant.pack(side=BOTTOM)
        
        #frame_bas.pack(side=BOTTOM,padx=5, pady=5)

        
        ###########
        ##Fenêtre##
        ###########     
    
        fenetre_choix_difficulte.mainloop() #boucle infinie fenetre
    
    def interface_menu():
        remarque="à faire"
        #http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
    def interface_graph_grille():
        fenetre_titre="Grille demineur"    
        
        fenetre_grille = Tk() #création de la fenetre
        fenetre_grille.title(fenetre_titre) #titre fenetre
        
        ########
        #Frames#
        ########
        frame_menu=interface_menu()
        frame_haut=Frame(fenetre_choix_difficulte)
        frame_bas=Frame(fenetre_choix_difficulte)
        
        
        
        
        
        ##############
        #Test logique#
        ##############
    if fonction=="choix_difficulte":
        return(interface_graph_difficulte())
        ##
        #print("choix_difficulte")
        ##
        
    elif fonction=="grille":
        return(interface_graph_grille())
        ##
        #print("grille")
        ##
        
    elif fonction=="resultat":
        ##
        #print("resultat")
        ##
        return(interface_graph_resultat())          



















"""
Menu=Tk()
Menu.geometry("300*300")
Menu.title("menu du demineur")
bouton=Button(Menu,text='facile',width=20,height=3,bg='green', command=fenetre.open)
bouton=Button(Menu,text='normal',width=20,height=3,bg='blue', command=fenetre2.open)
bouton=Button(Menu,text='expert',width=20,height=3,bg='red', command=fenetre3.open)

fenetre=Tk()
fenetre.geometry(550*600)
zone_dessin=Canvas(fenetre,width=550,height=1000,bg='white')
zone_dessin.place(x=10,y=20)
xgrille=10
ygrille=10
for i in range (0,xgrille+1):    
    zone_dessin.create_line(20+50*i,50,20+50*i,50+50*(ygrille))
 
for i in range(0,ygrille+1):
    zone_dessin.create_line(20,50+50*i,20+50*(xgrille),50+50*i)
  
fenetre.mainloop() 

fenetre2=Tk()
fenetre2.geometry(550*600)
zone_dessin=Canvas(fenetre2,width=550,height=1000,bg='white')
zone_dessin.place(x=10,y=20)
xgrille=16
ygrille=16
for i in range (0,xgrille+1):    
    zone_dessin.create_line(20+50*i,50,20+50*i,50+50*(ygrille))
 
for i in range(0,ygrille+1):
    zone_dessin.create_line(20,50+50*i,20+50*(xgrille),50+50*i)
  
fenetre2.mainloop() 

fenetre3=Tk()
fenetre3.geometry(550*600)
zone_dessin=Canvas(fenetre3,width=550,height=1000,bg='white')
zone_dessin.place(x=10,y=20)
xgrille=30
ygrille=16
for i in range (0,xgrille+1):    
    zone_dessin.create_line(20+50*i,50,20+50*i,50+50*(ygrille))
 
for i in range(0,ygrille+1):
    zone_dessin.create_line(20,50+50*i,20+50*(xgrille),50+50*i)
  
fenetre3.mainloop() 
"""

