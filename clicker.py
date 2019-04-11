import time
from tkinter import Tk, Button, Label, Text, END
from threading import Thread


counter = 0
plus_ = 1
check = False
check_gun = False
check_rifle = False
check_barret = False
check_vest = False
rifle_price = 7500
barret_plus = 1
end = 10000000
gun_price = 250
barret_price = 100
vest_price = 10000


root = Tk()
root.title("Press F to pay respect")
root.geometry('750x500+0+0')
text = Text(font = ('Times', '31', 'bold'))
text.insert(1.0, "collect all things of capitan Price")


def calculate(event):
    global end
    global counter
    text.delete(1.0, END)
    text.insert(1.0, "Respects payed: " + str(counter))


def plus(event):
    global counter
    global plus_
    counter += plus_
    calculate(event=None)


def buy_gun():
    global counter
    global plus_
    global gun_price
    global check_gun

    if counter < gun_price:
        return
    else:
        check_gun = True
        counter -= gun_price
        plus_ += 10
        gun_price += 150
        text.delete(1.0, END)
        text.insert(1.0, "Respects payed: " + str(counter))
        GunButton['text'] = "     buy respect gun: " + str(gun_price) + "     "


def buybarret():
    global counter
    global barret_price
    global burret_plus
    global end
    global check
    global check_barret

    counter -= barret_price
    while True:
        if check is True:
            break
        counter += barret_plus
        calculate(event=None)
        time.sleep(1)


def buy_barret():
    global barret_plus
    global counter
    global barret_price
    global check_barret
    if counter < barret_price:
        return
    else:
        check_barret = True
        if barret_plus == 1:
            barret_plus += 4
            Thread(target=buybarret).start()
        else:
            counter -= barret_price
            barret_plus += 1


def quit_():
    global check
    check = True
    sys.exit()


def f():
    global check
    check = True
    sys.exit()


def endgame():
    global counter
    global end
    global check_gun
    global check
    global check_rifle
    if (counter < end) or (check_gun is False) or (check_barret is False)\
            or (check_vest is False) or (check_rifle is False):
        return
    else:
        counter -= end
        window = Tk()
        window.title("Congratulations!")
        window.geometry('800x640+0+0')
        label = Label(window, text="Finally, you funeraled capitan Price.", font=("Helvetica", 20), fg = 'black')
        b = Button(window, text="F", font=("Times", 60, 'bold'), fg='red', command = f)
        label.place(x=70, y=0)
        b.place(x=100, y=100)


def wait():
    time.sleep(5)


def vest():
    Thread(target=buy_vest).start()


def buy_vest():
    global plus_
    global barret_plus
    global counter
    global check_vest
    if counter < vest_price:
        return
    counter -= vest_price
    check_vest = True
    t1 = plus_
    plus_ *= 2
    t2 = barret_plus
    barret_plus *= 2
    time.sleep(10)
    plus_ -= t1
    barret_plus -= t2
    return


def rifle():
    global counter
    global rifle_price
    global check_rifle
    global plus_
    if counter < rifle_price:
        return
    else:
        check_rifle = True
        counter -= rifle_price
        plus_ *= 2


def tutorial():
    t_w = Tk()
    t_w.title("Tutorial")
    t_w.geometry('800x400+50+50')
    t_l = Label(t_w, text="Respect gun gives you +10 score per click for each purchase;" + '\n' +
                          "Respect barret gives five score per second for each purchase;" + '\n' +
                          "Respect bulletproof vest activates double score bonus for each previous " 
                          "purchase for 10 seconds;" +
                          '\n' + "Respect rifle magnifies respects per click twice;" +
                          '\n' + "To win, you neeed to collect all capitan equipment, get 10000000"
                                 " respects and also end the funeral.",
                font=("Times", 15)
                )
    t_l.pack()


GunButton = Button(text="     buy respect gun: " + str(gun_price) + "      ",
                   bg='black', fg='green', font=('Times', '23', 'bold'),
                   width=21, command=buy_gun
                   )

BarretButton = Button(text="   buy respect barret: " + str(barret_price) + "    ",
                      bg='black', fg='green', font=('Times', '23', 'bold'),
                      width=21, command=buy_barret
                      )

VestButton = Button(text="     buy respect vest: " + str(vest_price) + "      ",
                    bg='black', fg='green', font=('Times', '23', 'bold'), width=21, command=vest
                    )

WinButton = Button(text="End cap's funeral", bg='black',
                   fg='yellow', font=('Times', '25', 'bold'), width=20, command=endgame
                   )

TutorialButton = Button(text="Tutorial", bg='grey', fg='white',
                        font=('Times', '17'), command=tutorial
                        )

Quit = Button(text="   quit   ", bg='grey', fg='white',
              font=('Times', '17'), command=quit_
              )

Heavy = Button(text="    buy respect rifle: " + str(rifle_price) + "    ",
               bg='black', fg='green', font=('Times', '23', 'bold'),
               width=21, command=rifle
               )


root.bind("<space>", plus)

GunButton.place(x=0, y=180)

BarretButton.place(x=0, y=240)

TutorialButton.place(x=0, y=134)

VestButton.place(x=0, y=303)

Quit.place(x=110, y=134)

Heavy.place(x=0, y=365)

WinButton.pack()

text.pack()

root.mainloop()
