###############################################################################
#Informations du module
###############################################################################
#Module graphique
#Objectif : créations des interfaces du programme, interraction avec l'utilisateur


###############################################################################
#Importation des modules
###############################################################################
from tkinter import * #bibliothèque graphique
from prop import * #nécéssaire pour le fonction difficulté

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
        
        ################
        #actions bouton#
        ################
        def difficulte_facile():
            xybombe.extend((9,9,10,40)) #grille 9x9, 10bombes, 40px de coté (case)
            print("fonction difficulté -> facile")
            fenetre_choix_difficulte.destroy() #détruit la fenetre pour executer le code qui suit
            #print("fenetre détruite") 
            
        def difficulte_inter():
            global xybombe
            xybombe.extend((16,16,40,35))
            print("fonction difficulté -> inter")
            fenetre_choix_difficulte.destroy()
            #print("fenetre détruite")
            
        def difficulte_expert():
            global xybombe
            xybombe.extend((30,16,99,25))
            print("fonction difficulté -> expert")
            fenetre_choix_difficulte.destroy()
            #print("fenetre détruite")
            
        
        fenetre_choix_difficulte.title(fenetre_titre) #titre fenetre
        ########
        #Frames#
        ########
        frame_haut=Frame(fenetre_choix_difficulte) #cadre du haut
        
        #########
        #Boutons#
        #########
        bouton_facile=Button(frame_haut,text='Facile',width=15,height=3,command=difficulte_facile) #bouton=bouton(dans le cadre "frame_haut",longueur=15,hauteur=3, assigné a la fonction difficulte_facile)
        bouton_facile.pack(side=LEFT,padx=5,pady=5) #alignement à gauche 5px sur les cotés
        
        bouton_intermediaire=Button(frame_haut,text='Intermediaire',width=15,height=3,command=difficulte_inter)
        bouton_intermediaire.pack(side=LEFT,padx=5,pady=5)
        
        bouton_expert=Button(frame_haut,text='Expert',width=15,height=3,command=difficulte_expert)
        bouton_expert.pack(side=LEFT,padx=5,pady=5)
        
        frame_haut.pack(side=TOP,padx=5, pady=5) #affichage du cadre(haut)  
        fenetre_choix_difficulte.mainloop() #boucle infinie fenetre       
        
    def interface_graph_grille():
        fenetre_titre="Grille demineur"  
        
        ###########
        #Variables#
        ###########
        global xybombe
        xgrille=xybombe[0]
        ygrille=xybombe[1]
        L_H_case_px=xybombe[3] #bord d'une case 
        fenetre_taille=str(15+(xgrille*L_H_case_px))+"x"+str(ygrille*L_H_case_px+15) # renvoi du texte ex: "300x800"
            
        #########
        #Fenêtre#
        #########
        fenetre_grille = Tk() #création de la fenetre
        fenetre_grille.title(fenetre_titre) #titre fenetre
        fenetre_grille.geometry(fenetre_taille) #défini la taille en px de la fenetre
        
        #######
        #Frame#
        #######
        frame_grille=Frame(fenetre_grille) #créer le cadre qui contiendra la grille (canvas)
        #frame_bas=Frame(fenetre_grille)
        
        
        ###########
        #Fonctions#
        ###########
        def aff_nb_bombe(xgrille,ygrille):
            """ Renvoi le nombre de bombe pour la case sélecionnée """
        remarque="a faire"
        
        def plein_ecran_F11():
            #fenetre_grille.geometry(fenetre_taille_plein_ecran)
            #fenetre_grille.overrideredirect(TRUE) #Supprime la bar de titre
            fenetre_taille_plein_ecran=str(fenetre_grille.winfo_screenwidth())+"x"+str(fenetre_grille.winfo_screenheight())+"+0+0"
            print(fenetre_taille_plein_ecran)      
            remarque="a corriger: commande s'exécute dès le lancement de la fenetre"
        ###########
        #FrameMenu#
        ###########
        bar_menu=Menu(fenetre_grille) #Ligne qui contient les menus (collé au haut de la fenetre)
        
        menu_fichier=Menu(bar_menu, tearoff=0) #menu non détachabke (tearoff=0 -> http://python.developpez.com/faq/?page=Menu#Comment-permettre-ou-non-qu-un-menu-soit-detachable-de-son-parent)
        menu_fichier.add_command(label="Label 1")
        menu_fichier.add_command(label="Label 2")
        menu_fichier.add_command(label="Label 3")
        menu_fichier.add_separator() #Afiche un trait de séparation
        menu_fichier.add_command(label="Quitter", command=fenetre_grille.destroy)        
        bar_menu.add_cascade(label="Fichier", menu=menu_fichier) # ajout du menu
        
        menu_affichage=Menu(bar_menu, tearoff=0)
        menu_affichage.add_command(label="Mode plein écran    F11", postcommand=plein_ecran_F11())
        
        menu_choix_couleur=Menu(menu_affichage, tearoff=0)
        menu_choix_couleur.add_command(label="Choix 1")
        menu_choix_couleur.add_command(label="Choix 2")
        menu_choix_couleur.add_command(label="Choix 3")
        menu_affichage.add_cascade(label="Choix couleur", menu=menu_choix_couleur, underline=0) #sous-menu, surligné quand sélectionné
        bar_menu.add_cascade(label="Affichage", menu=menu_affichage)
        
        
        menu_aide=Menu(bar_menu, tearoff=0)
        menu_aide.add_command(label="Documentation du demineur    F1")
        menu_aide.add_command(label="Tutoriel du démineur")
        menu_aide.add_separator()
        menu_aide.add_command(label="A propos")        
        
        bar_menu.add_cascade(label="Aide", menu=menu_aide) # ajout de menu
        fenetre_grille.config(menu=bar_menu)
        
        ########################
        #Affichage de la grille#
        ########################
        canvas_grille=Canvas(frame_grille,width=xgrille*50-1, height=ygrille*50-1)
        canvas_grille.pack(side=TOP) #Affiche le canvas (5px de côté)
        
        """
        A savoir : 1 case=50x50px
        """
        for h_ligne in range (ygrille+1): #Creation des lignes horizontales        
            x_debut=0
            x_fin=L_H_case_px*xgrille
            y_debut=y_fin=h_ligne*L_H_case_px
            canvas_grille.create_line(x_debut,y_debut,x_fin,y_fin) #crée la ligne
            
        for v_ligne in range(xgrille+1): #creation des lignes verticales    
            x_debut=x_fin=v_ligne*L_H_case_px
            y_debut=0
            y_fin=L_H_case_px*ygrille
        
            canvas_grille.create_line(x_debut,y_debut,x_fin,y_fin) #crée la ligne
        
        canvas_grille.create_line(0,2,L_H_case_px*xgrille,2) #ligne horizontale haut
        canvas_grille.create_line(2,0,2,L_H_case_px*ygrille) #ligne verticale gauche
        
        frame_grille.pack(side=TOP,padx=5,pady=5)
        fenetre_grille.mainloop()
        
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