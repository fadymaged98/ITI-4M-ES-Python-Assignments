from tkinter import *

sen_counter = 0
neth_counter = 0


def sen_goal():
    global sen_counter
    sen_counter += 1
    sen_score_label.configure(text=sen_counter)
    print("Senegal Has Scrored!", sen_counter)


def neth_goal():
    global neth_counter
    neth_counter += 1
    neth_score_label.configure(text=neth_counter)
    print("Ntherlands Has Scrored!", neth_counter)


window = Tk()

window.title("World Cup Matches")
window.geometry('500x500')
window.configure(bg='lemonchiffon')

senegal_img = PhotoImage(file='Flag_of_Senegal.png')
senegal_img = senegal_img.subsample(6, 6)

nether_img = PhotoImage(file='Netherlands.png')
nether_img = nether_img.subsample(17, 17)

senegal_label = Label(window, image=senegal_img, border='4', background='black')
nether_label = Label(window, image=nether_img, border='4', background='black', relief='raised')

senegal_label.place(x=50, y=50)
nether_label.place(x=290, y=50)

senegal_btn = Button(window, text="Senegal's Goal!", font=("Goudy Stout", 7), width=15, height=3, bg='lime green',
                     command=sen_goal)
nether_btn = Button(window, text="Netherl's Goal!", font=("Goudy Stout", 7), width=15, height=3, bg='dodgerblue3',
                    command=neth_goal)

quit_btn = Button(window, text="QUIT",  font=("Goudy Stout", 7),width=5, height=2, bg='red', command=window.destroy)


senegal_btn.place(x=40, y=250)
nether_btn.place(x=285, y=250)

quit_btn.place(x=400, y=450)

sen_score_label = Label(window, border='4', background='white', relief='raised', font=("Goudy Stout", 7), width=10,
                        text=0)
neth_score_label = Label(window, border='4', background='white', relief='raised', font=("Goudy Stout", 7), width=10,
                         text=0)

sen_score_label.place(x=65, y=350)
neth_score_label.place(x=315, y=350)

window.mainloop()
