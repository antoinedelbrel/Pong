from tkinter import*

fenetre = Tk()
fenetre.title('pong')

canvas = Canvas(fenetre, width = 725, height = 500, bg = 'black')

button_quitter = Button(fenetre, text = 'Quitter', command = fenetre.destroy)

#creation de la balle
ball = canvas.create_oval(342.5,230,382.5,270, fill = 'red')

#creation raquette
raquette_droite = canvas.create_rectangle(725,200,700,300, fill = 'white')
raquette_gauche = canvas.create_rectangle(25,200,0,300, fill = 'white')

button_quitter.pack()
canvas.pack()


fenetre.mainloop()