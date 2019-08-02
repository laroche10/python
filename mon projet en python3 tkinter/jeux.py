
#importation de tkinter, l'icon, le titre
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("le meilleur jeux de chance!!")
tk.iconbitmap("logo_N.ico")

#declaration des variable qui vont recevoir des valeurs bientôt
pa = StringVar()
joueurb = StringVar()
p1 = StringVar()
p2 = StringVar()
#les champs des noms des joeurs pas des case à remplir avec Textvariable qui va prendre les valeurs par la fonction StrindVar()

joueur1_nom = Entry(tk, textvariable=p1, bd=5)
joueur1_nom.grid(row=1, column=1, columnspan=8)
joueur2_nom = Entry(tk, textvariable=p2, bd=5)
joueur2_nom.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0
#la fonction BoutonDesactiver va permettre de desactiver les boutons au debut du jeux

def BoutonDesactiver():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, joueur2_nom, joueur1_nom, joueurb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        joueurb =  p2.get()   +  " félicitation vous avez Gagné le Paris!  " +  ' ' + p1.get() + " a échoué"
        pa =     p1.get()     +  " félicitation vous avez Gagné le Paris!  "+ ' '+ p2.get() + " a échoué"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showerror("trichez pas SVP!!", "Vous avez déjà cliquez!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        BoutonDesactiver()
        tkinter.messagebox.showinfo("Resultat Final", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Resultat Final", "match très chaud vous êtes à égalité")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        BoutonDesactiver()
        tkinter.messagebox.showinfo("Resultat Final", joueurb)


buttons = StringVar()
#le label qui va nous permettre de mettre la couleur , la hauteur , la largeur et le format de l'ecriture des joueurs

label = Label( tk, text="Joueur N°1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Joueur N°2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

#les boutons du jeux, couleur, commande etc.....


button1 = Button(tk, text=" ", font='Times 20 bold', bg='orange', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='orange', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='orange', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)
tkinter.messagebox.showinfo('PLAY','Vous allez commencer le jeux, être vous prêt?')

tk.mainloop()