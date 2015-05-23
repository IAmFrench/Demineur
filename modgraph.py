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
from modclic import *
from modcases import * #nécéssaire pour la fonction statut_case_texte()

###############################################################################
#fonctionnalitées du module du module
###############################################################################
xygrille_liste=["-1x-1"]
case_dec=["0"]


def taille_cases_plein_ecran(taille_x_ecran,taille_y_ecran):
    """ calcule la taille des cases en fonction de la taille de l'écran de l'utilisateur """
    #taille_x_ecran=taille_x_ecran #Taille horizontale en px de l'écran (ex:1920)
    #taille_y_ecran=taille_y_ecran #Taille verticale en px de l'écran (ex:1080)
    
    ###########################
    #Importation des variables#
    ###########################
    global xybombe #Nécéssaire pour savoir le nombre de case en fonction de la difficulté choisie
    
    ##############
    #Test logique#
    ##############
    #print(xybombe)    
        
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
            global statut_plein_ecran #savoir le statut en cours (True/False)
            taille_x_ecran=fenetre_grille.winfo_screenwidth() #Taille horizontale de l'écran
            taille_y_ecran=fenetre_grille.winfo_screenheight() #Taille verticale de l'écran
            fenetre_taille_plein_ecran=str(taille_x_ecran)+"x"+str(taille_y_ecran) #+"+0+0" #Taille de la fenetre en plein ecran, résultat sous forme de chaine de caractère, (ex:1920x180)
            
            ##############
            #Test logique#
            ##############
            if statut_plein_ecran==False: #Alors activé le plein ecran
                for compteur in range(0,2):
                    print(compteur)                
                    fenetre_grille.geometry(fenetre_taille_plein_ecran) #Modifie la taille de la fenetre
                    taille_cases_plein_ecran(taille_x_ecran,taille_y_ecran) #modifie la taille des cases
                fenetre_grille.overrideredirect(TRUE) #Supprime la bar de titre
            elif statut_plein_ecran==True: #Désactiver le plein ecran
                fenetre_grille.geometry(fenetre_taille)
            else:
                print("Erreur Fonction Plein Ecran")
            fenetre_taille_plein_ecran=str(taille_x_ecran)+"x"+str(taille_y_ecran) #+"+0+0" #Taille de la fenetre en plein ecran, résultat sous forme de chaine de caractère, (ex:1920x180)
            fenetre_grille.geometry(fenetre_taille_plein_ecran) #Modifie la taille de la fenetre
            fenetre_grille.overrideredirect(TRUE) #Supprime la bar de titre
            taille_cases_plein_ecran(taille_x_ecran,taille_y_ecran) #modifie la taille des cases
            remarque="a finir"

       # def decouvre():
          #   for cle in grille:
             #    case=grille[cle]
              #   if case[3]==6:#
                     #   if cle is not case_dec:
                       #     case_dec.append(cle)                         
                        #    case_visuel(cle)   
        def decou(liste):
            for cle in liste:
                case_visuel(cle)
    
        def pointeurG(event):
            global cases_modif
            
            if xybombe[0]==9:
                xygrille=coord(event.x,event.y,"facile") #les coordonnées en pixels sont convertie en coordonné de case par coord
            
            if xybombe[0]==16:
                xygrille=coord(event.x,event.y,"intermediaire")  
        
            if xybombe[0]==30:
                xygrille=coord(event.x,event.y,"expert")
            
            print("Clic gauche sur la case "+xygrille)
            camo[:] = []
            camo.append(xygrille)
            clic0(xygrille)            
            decou(camo)
            xygrille_liste[0]=xygrille #assigne a la variable xygrille_liste la case cliqué
            
        def pointeurD(event):
            if xybombe[0]==9:
                xygrille=coord(event.x,event.y,"facile")
            
            if xybombe[0]==16:
                xygrille=coord(event.x,event.y,"intermediaire")
            
            if xybombe[0]==30:
                xygrille=coord(event.x,event.y,"expert")
            clic1(xygrille)
            print("Clic droit sur la case "+xygrille)
            xygrille_liste[0]=xygrille
            case_visuel(xygrille)
            
        def coordonne_case(xygrille):
            global xybombe
            #############
            #Explication#
            #############
            #Renvoi sous forme de dictionnaire/liste les coordonnées des 4 extrémités d'une case donnée
            #Exemple : coordonne_case(1x1) -> {A:[1,1],B:[1,24],C:[24,1],D:[24,24]}
            dico_coord={} #Création du dico vide
            points=['haut_gauche','bas_droite']
            a=0
            for point in points: #parcours les elements de la liste des points
                xgrille=ext_xy(xygrille,"x") #Extraction coordonnée x de la case (ex:8x12 -> 8)
                ygrille=ext_xy(xygrille,'y') #Extraction coordonnée y de la case (ex:8x12 -> 12)        
                if a==0: #fait dans un premier temps x/y haut_gauche
                    xgrille=xgrille-1
                    ygrille=ygrille-1
                    x=xybombe[3]*xgrille #Calcul
                    y=xybombe[3]*ygrille #Calcul
                    xycoord=[x+1,y+1] #Assemblage
                    dico_coord[point]=xycoord #Intégration dans le dico
                if a==1:
                    x=xybombe[3]*xgrille #Calcul
                    y=xybombe[3]*ygrille #Calcul
                    xycoord=[x-1,y-1] #Assemblage
                    dico_coord[point]=xycoord #Intégration dans le dico
                a=1
                #print(xycoord)
                
            return(dico_coord) #Retourne le dico
        ###########
        #FrameMenu#
        ###########
        bar_menu=Menu(fenetre_grille) #Ligne qui contient les menus (collé au haut de la fenetre)
        
        #Groupe 1
        menu_fichier=Menu(bar_menu, tearoff=0) #menu non détachabke (tearoff=0 -> http://python.developpez.com/faq/?page=Menu#Comment-permettre-ou-non-qu-un-menu-soit-detachable-de-son-parent)
        menu_fichier.add_command(label="Label 1")
        menu_fichier.add_command(label="Label 2")
        menu_fichier.add_command(label="Label 3")
        menu_fichier.add_separator() #Afiche un trait de séparation
        menu_fichier.add_command(label="Quitter", command=fenetre_grille.destroy)        
        bar_menu.add_cascade(label="Fichier", menu=menu_fichier) # ajout du menu
        
        menu_affichage=Menu(bar_menu, tearoff=0)
        menu_affichage.add_command(label="Mode plein écran    F11") #, command=plein_ecran_F11
        
        #Groupe 2
        menu_choix_couleur=Menu(menu_affichage, tearoff=0)
        menu_choix_couleur.add_command(label="Choix 1")
        menu_choix_couleur.add_command(label="Choix 2")
        menu_choix_couleur.add_command(label="Choix 3")
        menu_affichage.add_cascade(label="Choix couleur", menu=menu_choix_couleur, underline=0) #sous-menu, surligné quand sélectionné
        bar_menu.add_cascade(label="Affichage", menu=menu_affichage)
        
        #Groupe 3
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
        canvas_grille=Canvas(frame_grille,width=xgrille*L_H_case_px-1, height=ygrille*L_H_case_px-1,background=couleur("defaut","r2"))
        canvas_grille.pack(side=TOP) #Affiche le canvas (5px de côté)
        
        #######################
        #Fonctions Dans canvas#    
        #######################
        def rectangle_canvas(x0,y0,x1,y1,propri):
            """ Crée le canvas rectangle """
            if propri == "bombe":
                rectangle_bombe_perdu=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r3"),outline=couleur("defaut","r3"))
            elif propri=="drapeau":
                rectangle_dapeau=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r5"),outline=couleur("defaut","r5"))
                canvas_id = canvas_grille.create_text(x0, y0, anchor="nw")

                canvas_grille.itemconfig(canvas_id, text="  |*")
                #canvas_grille.insert(canvas_id, 12)
            
            elif propri=="interrogation":
                remarque="a faire"
                rectangle_interro=canvas_grille.create_text(x0,y0,x1,y1,text="?")
            elif propri=="visible":
                rectangle_visible=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r4"),outline=couleur("defaut","r4")) #fill = couleur du rectangle(intérieur), outline = couleur de la bordure du rectangle
            elif propri=="chiffre":
                rectangle_dapeau=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r4"),outline=couleur("defaut","r4"))
                canvas_id = canvas_grille.create_text(x0, y0, anchor="nw")

                canvas_grille.itemconfig(canvas_id, text="1")
                
        def case_visuel(xygrille):
            #############
            #Explication#
            #############
            #Change la case de couleur/visuel
            #Fonction qui s'active dès l'appel de l'une des fonctions
            #PointeurG ou PointeurD            
            #xygrille=xygrille #la case cliqué
            
            #################################
            #Lire les coordonnées de la case#
            #################################
            #if xygrille != "-1x-1":
            coordcase=coordonne_case(xygrille) #charge les coordonnées des 2 points aux extrémités de la case (haut_gauche et bas_droite)
            prop_case=statut_case_texte(xygrille) #charge les propriétés de la case en question -> dico
            ############################    
            #Applique les modifications#
            ############################
            prop_possibles=["bombe","drapeau","interrogation","visible","chiffre"]
            for propri in prop_possibles:
                #print(prop_case[propri])
                if prop_case[propri]==True:
                    haut_gauche=coordcase["haut_gauche"] #retourne une liste, (ex:[177, 107])
                    x_haut_gauche=haut_gauche[0] #prend la première valeur de la liste (ex:177)
                    y_haut_gauche=haut_gauche[1] #Prend la seconde valeure de la liste (ex:107)
                    bas_droite=coordcase["bas_droite"] #idem que pour haut_gauche
                    x_bas_droite=bas_droite[0]
                    y_bas_droite=bas_droite[1]
                    rectangle_canvas(x_haut_gauche,y_haut_gauche,x_bas_droite,y_bas_droite,propri) #Fonction qui crée le canvas
                    
        #################
        #Création Grille#
        #################
        for h_ligne in range (ygrille+1): #Creation des lignes horizontales        
            x_debut=0 #coordonné x du point de départ
            x_fin=L_H_case_px*xgrille #coordonné x du point d'arrivé
            y_debut=y_fin=h_ligne*L_H_case_px #coordonné y du point de départ et d'arrivé (égaux car c'est une droite horizontale)
            canvas_grille.create_line(x_debut,y_debut,x_fin,y_fin,fill=couleur("defaut","r1")) #crée la ligne du point de départ au point d'arrivé
            
        for v_ligne in range(xgrille+1): #creation des lignes verticales    
            x_debut=x_fin=v_ligne*L_H_case_px
            y_debut=0
            y_fin=L_H_case_px*ygrille
        
            canvas_grille.create_line(x_debut,y_debut,x_fin,y_fin,fill=couleur("defaut","r1")) #crée la ligne
        
        canvas_grille.create_line(0,2,L_H_case_px*xgrille,2,fill=couleur("defaut","r1")) #ligne horizontale haut
        canvas_grille.create_line(2,0,2,L_H_case_px*ygrille,fill=couleur("defaut","r1")) #ligne verticale gauche
        frame_grille.pack(side=TOP,padx=5,pady=5) #(5px de côté)
        
        ##############
        #Clics souris#
        ##############
        canvas_grille.bind("<Button-1>",pointeurG) #Si clic gauche(.bind("<Button-1>")) alors exécute la fonction pointeurG
        canvas_grille.bind("<Button-3>",pointeurD) #Si clic droit alors exécute la fonction pointeurG
        fenetre_grille.mainloop() # boucle de la fenêtre
        
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