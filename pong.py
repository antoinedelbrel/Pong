from tkinter import*
from math import*

dx = 7
dy = 7

#mouvement de la balle
def jouer():
    global fenetre

    def move_ball():
        global dx, dy
        if canvas.coords(ball)[3] > 500 or canvas.coords(ball)[1] < 0:
            dy *= -1
        if len(canvas.find_overlapping(canvas.coords(raquette_droite)[0], canvas.coords(raquette_droite)[1], canvas.coords(raquette_droite)[2], canvas.coords(raquette_droite)[3])) > 1:
            dx *= -1
        if len(canvas.find_overlapping(canvas.coords(raquette_gauche)[0], canvas.coords(raquette_gauche)[1], canvas.coords(raquette_gauche)[2], canvas.coords(raquette_gauche)[3])) > 1:
            dx *= -1
            
            
        canvas.move(ball, dx, dy)
        fenetre.after(20, move_ball)           

    canvas = Canvas(fenetre, width = 725, height = 500, bg = 'black')

    #creation de la balle
    ball = canvas.create_oval(342.5,230,382.5,270, fill = 'red')

    #creation raquette
    raquette_droite = canvas.create_rectangle(725,200,700,300, fill = 'white')
    raquette_gauche = canvas.create_rectangle(25,200,0,300, fill = 'white')

    #on fait bouger les raquettes
    def droite_haut(event):
        canvas.move(raquette_droite, 0, -10)

    def droite_bas(event):
        canvas.move(raquette_droite, 0, 10)
    
    def gauche_haut(event):
        canvas.move(raquette_gauche, 0, -10)

    def gauche_bas(event):
        canvas.move(raquette_gauche, 0, 10)

    canvas.bind_all('<Up>', droite_haut)
    canvas.bind_all('<Down>', droite_bas)
    canvas.bind_all('<a>', gauche_haut)
    canvas.bind_all('<q>', gauche_bas)

    canvas.pack()
       
    move_ball()   

fenetre = Tk()
fenetre.title('pong')

button_quitter = Button(fenetre, text = 'Quitter', command = fenetre.destroy)


button_quitter.pack()

button_jouer = Button(fenetre, text = 'Jouer', command = jouer)
button_jouer.pack()


fenetre.mainloop()