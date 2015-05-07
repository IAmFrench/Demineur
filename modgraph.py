#Module graphique

from tkinter import *
from core import *
from modegrille import *
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

