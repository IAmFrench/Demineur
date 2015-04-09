#Module graphique

from tkinter import *
fenetre=Tk()
fenetre.geometry("1500x1500")
zone_dessin=Canvas(fenetre,width=1000,height=1000,bg='white')
xgrille=8
ygrille=10
zone_dessin.place(x=10,y=20)
for i in range (0,xgrille):
    
    zone_dessin.create_line(20+50*i,50,20+50*i,50+50*(ygrille+1))
    zone_dessin.create_line(20,50+50*i,50+50*(xgrille+1),50+50*i)
fenetre.mainloop()
