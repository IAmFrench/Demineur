###############################################################################
#Informations du module
###############################################################################
#Module graphique
#Objectif : créations des interfaces du programme, interraction avec l'utilisateur


###############################################################################
#Importation des modules
###############################################################################
from tkinter import * #bibliothèque graphique
from tkinter.messagebox import * # boîte de dialogue
from prop import * #nécéssaire pour le fonction difficulté
from modclic import *
from modcases import * #nécéssaire pour la fonction statut_case_texte()

###############################################################################
#fonctionnalitées du module du module
###############################################################################
xygrille_liste=["-1x-1"]
case_dec=["0"]
liste_bombes=[] #liste de toutes les cases qui contiennent une bombe
liste_cases_visibles=[] #liste des cases visibles
show=[0] #fonction show_all_bbs pas encore demandé
version="1.0.0" #version en cours du démineur

def statut_partie():
    """ renvoi le statut de la partie\n 3 possibilités :\n-Gagnée,\n-Perdue,\n-En cours. """
    global liste_bombes #case qui contiennent des bombes
    global liste_cases_visibles #les cases dévoilées depuis le début
    global xybombe #pour le nombre de cases et le bombre de bombes bref pour tout
    au_cas_ou=True
    for case_bombe in liste_bombes:
        if case_bombe in liste_cases_visibles: #si une case qui contient une bombe se trouve dans la liste des cases visibles alors le joueur a perdu
            au_cas_ou=False            
            return("Perdue") #perduE car unE partie
    #si le joueur a perdu la fonction s'arrète là    
    
    if au_cas_ou==True: #si la fonction ne s'arrète pas et que le joueur a perdu
        taille_liste=len(liste_cases_visibles)
        taille_grille=xybombe[0]*xybombe[1]
        if taille_liste==taille_grille-xybombe[2]: #taille de la grille mois le nombre de bombes
            return("Gagnée") #éE -> meme remarque pour pour perdue
        else: #si la taille de la liste est différente de la taille de la grille ([0] et [1]) moins le bombre de bombes ([2])
            return("En cours")        
     
def gagne_ou_perdu():
    """ Effectue une action en fonction du résultat de la partie """
    texte_msg="defaut"
    #Contenue de la boite de dialogue
    statut=statut_partie()
    print(statut)
    if statut=="Gagnée":
        texte_msg="Bravo !\nVous avez gagné\n"
        print(texte_msg)
    if statut=="Perdue":
        texte_msg="Vous ferez mieux la prochaine fois\n"
        print(texte_msg)
    if texte_msg!="defaut": #si le joueur a gagné ou perdu alors:
        #On va créer une boite de dialogue qui affiche le texte_msg et un bouton pour quitter
        showinfo("Partie "+statut,texte_msg) #voilà c'est tout !

def f1_ie_docu(event): #nécéssaire de créer cette focntion car ie_docu ne prend pas en argument un évement
    """ si touche F1 enfoncé ouvre lapage d'aide (documentation) """
    ie_docu()
    
def ie(url):
    """ ouvre une page web (donnée en argument) """
    import webbrowser
    webbrowser.open(url) #mieux car permet d'ouvrir avec le navigateur par défaut
    
def ie_docu():
    """ ouvre la page d'aide """
    ie("https://github.com/IAmFrench/Demineur/wiki")

def ie_tuto():
    """ ouvre la page de tuto """
    ie("https://github.com/IAmFrench/Demineur/wiki")

def a_propos():
    """ ouvre une fenetre graphique a propos du programme """
    global version #pour le n° de version
    fenetre_a_propos=Tk()
    frame_haut=Frame(fenetre_a_propos)
    frame_haut.pack()
    frame_bas=Frame(fenetre_a_propos)
    frame_bas.pack()
    
    titre=Label(frame_haut,text="Demineur")
    titre.pack()
    ss_titre=Label(frame_haut,text="Un démineur codé en python\n")
    ss_titre.pack()
    description=Label(frame_haut,text="Copyright © 2015\nAlexandre Parès,\nRaphaël Gurerin et\nAlexandre Quintais\n")
    description.pack()
    licence=Label(frame_haut,text="Sous licence CC BY-NC-ND 3.0\n")
    licence.pack()
    version2=Label(frame_haut,text="Vous utilisez la version "+version+" du démineur\n")
    version2.pack()
    button=Button(frame_bas,text="Fermer",command=fenetre_a_propos.destroy)
    button.pack()
    fenetre_a_propos.mainloop()

def graph_fenetre(fonction):
    """ Ouvre la fenetre graphique qui correspond a la fonction donnée en argument """
    """
    liste des valeur pour fonction :
    - choix_difficulte
    - grille
    - resultat
    """
    
    ###########################################################################
    #Creation fenetre choix difficulté (#1)
    ###########################################################################
    def interface_graph_difficulte():
        """ Ouvre la fenetre du choix de difficulté """
        fenetre_titre="Choix Difficulté" #titre de la fenetre (seulement une variable)
        
        fenetre_choix_difficulte = Tk() #création de la fenetre        
        fenetre_choix_difficulte.title(fenetre_titre) #assignation du titre de la fenetre
        
        ################
        #actions bouton#
        ################
        def difficulte_facile():
            """ attribue les caractéristiques d'une grille de niveau facile """
            xybombe.extend((9,9,10,40,"facile")) #grille 9x9, 10bombes, 40px de coté (case)
            print("fonction difficulté -> facile")
            fenetre_choix_difficulte.destroy() #détruit la fenetre pour executer le code qui suit
            print("fenêtre choix détruite") 
            
        def difficulte_inter():
            """ attribue les caractéristiques d'une grille de niveau intermediaire """
            global xybombe
            xybombe.extend((16,16,40,35,"intermediaire"))
            print("fonction difficulté -> inter")
            fenetre_choix_difficulte.destroy()
            print("fenêtre choix détruite")
            
        def difficulte_expert():
            """ attribue les caractéristiques d'une grille de niveau expert """
            global xybombe
            xybombe.extend((30,16,99,25,"expert"))
            print("fonction difficulté -> expert")
            fenetre_choix_difficulte.destroy()
            print("fenêtre choix détruite")
            

        
        ########
        #Frames#
        ########
        frame_haut=Frame(fenetre_choix_difficulte) #cadre du haut
        frame_haut.pack(side=TOP,padx=5, pady=5) #affichage du cadre(haut)
        
        #########
        #Boutons#
        #########
        bouton_facile=Button(frame_haut,text='Facile',width=15,height=3,command=difficulte_facile) #bouton=bouton(dans le cadre "frame_haut",longueur=15,hauteur=3, assigné a la fonction difficulte_facile)
        bouton_facile.pack(side=LEFT,padx=5,pady=5) #alignement à gauche 5px sur les cotés
        
        bouton_intermediaire=Button(frame_haut,text='Intermediaire',width=15,height=3,command=difficulte_inter)
        bouton_intermediaire.pack(side=LEFT,padx=5,pady=5)
        
        bouton_expert=Button(frame_haut,text='Expert',width=15,height=3,command=difficulte_expert)
        bouton_expert.pack(side=LEFT,padx=5,pady=5)
        
        fenetre_choix_difficulte.mainloop() #boucle infinie fenetre       

    ###########################################################################
    #Creation fenetre grille demineur (#2)
    ###########################################################################        
    def interface_graph_grille():
        fenetre_titre="Grille demineur"
        
        ###########
        #Variables#
        ###########
        global xybombe
        xgrille=xybombe[0] #nombre de cases horizontalement (x)
        ygrille=xybombe[1] #nombre de cases verticalement (y)
        L_H_case_px=xybombe[3] #bord d'une case en px
        fenetre_taille=str(15+(xgrille*L_H_case_px))+"x"+str(ygrille*L_H_case_px+15) #renvoi du texte ex: "300x800"
        
        #########
        #Fenêtre#
        #########
        fenetre_grille = Tk() #création de la fenetre
        fenetre_grille.title(fenetre_titre) #assignation du titre de la fenetre
        fenetre_grille.geometry(fenetre_taille) #défini la taille en px de la fenetre
        
        #######
        #Frame#
        #######
        frame_grille=Frame(fenetre_grille) #créer le cadre qui contiendra la grille (canvas)
        
        
        ###########
        #Fonctions#
        ###########
        """
        Les fonctions qui se trouve ci-dessous sont définis ici car elle
        contiennent des variables qui ne sont pas définis en dehors de la
        fonction interface_graph_grille, tels que la variable de la fenetre
        graphique (fenetre_grille) ou le nom de la frame qui contient la grille
        (frame_grille)
        """
        
        def decou(liste):
            """ explication fonction """
            for cle in liste:
                case_visuel(cle,"gauche")
    
        def pointeurG(event):
            """ fonction qui est appellé lorsque qu'il y a un clic gauche dans le canvas_grille """
            global cases_modif
            
            if xybombe[4]=="facile":
                xygrille=coord(event.x,event.y,"facile") #les coordonnées en pixels sont convertie en coordonné de case par coord
            
            if xybombe[4]=="intermediaire":
                xygrille=coord(event.x,event.y,"intermediaire")  
        
            if xybombe[4]=="expert":
                xygrille=coord(event.x,event.y,"expert")
            
            camo[:] = []
            camo.append(xygrille)
            clic0(xygrille)            
            decou(camo)
            xygrille_liste[0]=xygrille #assigne a la variable xygrille_liste la case cliqué
            gagne_ou_perdu() #on effectue le test pour savoir si le joueur a gagné ou perdu
            if statut_partie()=="Perdue" or statut_partie()=="Gagnée":
                fenetre_grille.destroy()
                print("fenetre détruite")
            
        def pointeurD(event):
            """ fonction qui est appellé lorsque qu'il y a un clic droit dans le canvas_grille """
            if xybombe[0]==9:
                xygrille=coord(event.x,event.y,"facile")
            
            if xybombe[0]==16:
                xygrille=coord(event.x,event.y,"intermediaire")
            
            if xybombe[0]==30:
                xygrille=coord(event.x,event.y,"expert")
            clic1(xygrille)
            print("Clic droit sur la case "+xygrille)
            xygrille_liste[0]=xygrille
            case_visuel(xygrille,"droit")
            gagne_ou_perdu()
            if statut_partie()=="Perdue" or statut_partie()=="Gagnée":
                fenetre_grille.destroy()
                print("fenetre détruite")
                
        def coordonne_case(xygrille):
            """ renvoi sous forme d'un dictionnaire les coordonnées aux extrémités d'une case donnée (xygrille) """
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
                
            return(dico_coord) #Retourne le dico
        
        ###########
        #FrameMenu#
        ###########
        bar_menu=Menu(fenetre_grille) #Ligne qui contient les menus (collé au haut de la fenetre)
        
        #Groupe 1
        menu_fichier=Menu(bar_menu, tearoff=0) #menu non détachabke (tearoff=0 -> http://python.developpez.com/faq/?page=Menu#Comment-permettre-ou-non-qu-un-menu-soit-detachable-de-son-parent)
        #menu_fichier.add_command(label="Nouveau jeu")
        #menu_fichier.add_command(label="Difficulté")
        #menu_fichier.add_command(label="Label 3")
        #menu_fichier.add_separator() #Afiche un trait de séparation
        menu_fichier.add_command(label="Quitter", command=fenetre_grille.destroy)        
        bar_menu.add_cascade(label="Fichier", menu=menu_fichier) # ajout du menu
        
        menu_affichage=Menu(bar_menu, tearoff=0)
        menu_affichage.add_command(label="Mode plein écran    F11") #, command=plein_ecran_F11
        
        #Groupe 2
        #menu_choix_couleur=Menu(menu_affichage, tearoff=0)
        #menu_choix_couleur.add_command(label="defaut")
        #menu_choix_couleur.add_command(label="DarkBlue Red")
        #menu_choix_couleur.add_command(label="Flat design colors")
        #menu_affichage.add_cascade(label="Choix couleur", menu=menu_choix_couleur, underline=0) #sous-menu, surligné quand sélectionné
        #bar_menu.add_cascade(label="Affichage", menu=menu_affichage)
        
        #Groupe 3
        menu_aide=Menu(bar_menu, tearoff=0)
        menu_aide.add_command(label="Documentation du demineur    F1", command=ie_docu)
        menu_aide.add_command(label="Tutoriel du démineur", command=ie_tuto)
        menu_aide.add_separator()
        menu_aide.add_command(label="A propos",command=a_propos)        
        
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
        def rectangle_canvas(x0,y0,x1,y1,propri,xygrille):
            """ Crée le canvas rectangle """
            global xybombe
            ajustementx=(2/5)*xybombe[3]
            if xybombe[4]=="expert":
                ajustementy=(1/11)*xybombe[3]
            else :
                ajustementy=(1/4)*xybombe[3]
            if propri == "perdu":
                rectangle_bombe_perdu=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r3"),outline=couleur("defaut","r3"))
            elif propri=="drapeau":
                rectangle_dapeau=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r5"),outline=couleur("defaut","r5"))
                canvas_id = canvas_grille.create_text(x0+ajustementx, y0+ajustementy, anchor="nw")

                canvas_grille.itemconfig(canvas_id, text="|*")
                            
            elif propri=="interrogation":
                rectangle_dapeau=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r5"),outline=couleur("defaut","r5"))
                canvas_id = canvas_grille.create_text(x0+ajustementx, y0+ajustementy, anchor="nw")

                canvas_grille.itemconfig(canvas_id, text="?")
                
            elif propri=="visible":
                rectangle_visible=canvas_grille.create_rectangle(x0,y0,x1,y1,fill=couleur("defaut","r4"),outline=couleur("defaut","r4")) #fill = couleur du rectangle(intérieur), outline = couleur de la bordure du rectangle
            elif propri=="chiffre":
                case=grille[xygrille]
                if case[4]<=-1:
                    a="coucou" #NE SERT STRICTEMENT A RIEN
                else :
                    canvas_id = canvas_grille.create_text(x0, y0, anchor="nw")
                    canvas_grille.itemconfig(canvas_id, text=str(case[4]+1))

        def show_all_bbs():
            """ dévoile toute les bombes de la grille """
            #Ajoute les cases qui ont une  bombes dans une liste
            global liste_bombes #importe la liste
            #decou(liste_bombes)
        
        def case_visuel(xygrille,clic):
            """ permet de modifier visuellement les caractéristiques d'une cases """
            #############
            #Explication#
            #############
            #Change la case de couleur/visuel
            #Fonction qui s'active dès l'appel de l'une des fonctions
            #PointeurG ou PointeurD            
            #xygrille=xygrille #la case cliqué
            global show #nécéssaire pour éviter de faire une boucle infinie
            
            #################################
            #Lire les coordonnées de la case#
            #################################
            coordcase=coordonne_case(xygrille) #charge les coordonnées des 2 points aux extrémités de la case (haut_gauche et bas_droite)
            prop_case=statut_case_texte(xygrille) #charge les propriétés de la case en question -> dico
            
            ############################    
            #Applique les modifications#
            ############################
            prop_possibles=["bombe","drapeau","interrogation","visible","chiffre"]
            
            for propri in prop_possibles:
                #print(prop_case[propri])
                haut_gauche=coordcase["haut_gauche"] #retourne une liste, (ex:[177, 107])
                x_haut_gauche=haut_gauche[0] #prend la première valeur de la liste (ex:177)
                y_haut_gauche=haut_gauche[1] #Prend la seconde valeure de la liste (ex:107)
                bas_droite=coordcase["bas_droite"] #idem que pour haut_gauche
                x_bas_droite=bas_droite[0]
                y_bas_droite=bas_droite[1]
                
                if prop_case[propri]==True or type(prop_case[propri])==int: #si vrai ou si un chiffre
                    
                    if propri=="drapeau" or clic=="gauche" or propri=="interrogation":
                        rectangle_canvas(x_haut_gauche,y_haut_gauche,x_bas_droite,y_bas_droite,propri,xygrille) #Fonction qui crée le canvas
                    
                    if propri=="chiffre" and clic=="gauche":
                        if prop_case[propri]>-1:
                            rectangle_canvas(x_haut_gauche,y_haut_gauche,x_bas_droite,y_bas_droite,propri,xygrille)
                            if xygrille in liste_cases_visibles:
                                remarque=""
                            else:                                
                                liste_cases_visibles.append(xygrille)
                                
                    if propri=="visible" and prop_case["bombe"]==True: #si case visible et il y a une bombe alors le joueur a perdu donc case en rouge et pas encore demandé
                        if show[0]==0:
                            #fonction qui révèle toutes les bombes
                            show_all_bbs()
                            show[0]=1
                        rectangle_canvas(x_haut_gauche,y_haut_gauche,x_bas_droite,y_bas_droite,"perdu",xygrille)
                        
                if prop_case["drapeau"]==False and prop_case["visible"]==False and prop_case["interrogation"]==False:
                    rectangle_dapeau=canvas_grille.create_rectangle(x_haut_gauche,y_haut_gauche,x_bas_droite,y_bas_droite,fill=couleur("defaut","r2"),outline=couleur("defaut","r2"))
        
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
        
        ############
        #Evénements#
        ############
        canvas_grille.bind("<Button-1>",pointeurG) #Si clic gauche(.bind("<Button-1>")) alors exécute la fonction pointeurG
        canvas_grille.bind("<Button-3>",pointeurD) #Si clic droit alors exécute la fonction pointeurG
        fenetre_grille.bind("<F1>",f1_ie_docu) #evenement placé sour la fenetre principale car c'est sur elle qu'est enregistré la touche F1
        fenetre_grille.mainloop() # boucle de la fenêtre
        
    def interface_graph_resultat():
        """ fenetre résumé des scores, de la partie etc... """
        fenetre_score=Tk()

        remarque="a remplir"        
        
        fenetre_score.mainloop()
        
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
