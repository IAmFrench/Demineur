#Module graphique

from tkinter import *
from core import *
from modegrille import *
fenetre=Tk()
xgrille=str(input("que voulez vous?"))
ygrille=str(input("que voulez vous?"))
xgrille=int(xgrille)
ygrille=int(ygrille)
taille=str((xgrille*50+20))+"x"+str((ygrille*50+50))
fenetre.geometry(taille)
zone_dessin=Canvas(fenetre,width=550,height=1000,bg='white')
zone_dessin.place(x=10,y=20)
xgrille=10
ygrille=10
for i in range (0,xgrille+1):    
    zone_dessin.create_line(20+50*i,50,20+50*i,50+50*(ygrille))
 
for i in range(0,ygrille+1):
    zone_dessin.create_line(20,50+50*i,20+50*(xgrille),50+50*i)
  
fenetre.mainloop() 

