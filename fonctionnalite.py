# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:25:19 2015

@author: Alexandre
Bouts de code non utilisés, mais utiles pour toute amélioration du programme
"""

def taille_cases_plein_ecran(taille_x_ecran,taille_y_ecran):
    """ calcule la taille des cases en fonction de la taille de l'écran de l'utilisateur """
    #taille_x_ecran=taille_x_ecran #Taille horizontale en px de l'écran (ex:1920)
    #taille_y_ecran=taille_y_ecran #Taille verticale en px de l'écran (ex:1080)
    
    ###########################
    #Importation des variables#
    ###########################
    global xybombe #Nécéssaire pour savoir le nombre de cases en fonction de la difficulté choisie
    
    ##############
    #Test logique#
    ##############
    #print(xybombe)
    
    
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