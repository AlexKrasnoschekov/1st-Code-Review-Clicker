import time
from tkinter import *
from threading import Thread
counter = 0
plus = 1
check = False
check_gun = False
check_rifle = False
check_barret = False
check_vest = False
rifle_price = 10000
barret_plus = 1
end = 1000000
gun_price = 250
barret_price = 100
vest_price = 500
root = Tk()
root.title("Press F to pay respect")
root.geometry('600x400+0+0')
text = Text(font = ('Times', '31', 'bold'))
text.insert(1.0, "collect all things of capitan Price:")
def Calculate(event):
    global end
    global counter
    text.delete(1.0, END)
    text.insert(1.0, "Respects payed: " + str(counter))
def Plus(event):
    global counter
    global plus
    counter += plus
    Calculate(event = None)
def buy_gun():
    global counter
    global plus
    global gun_price
    global check_gun
    if (counter < gun_price):
        return
    else:
        check_gun = True
        counter -= gun_price
        plus += 10
        gun_price += 150
        text.delete(1.0, END)
        text.insert(1.0, "Respects payed: " + str(counter))
        GunButton['text'] = "buy respect gun: " + str(gun_price)
def BuyBarret():
    global counter
    global barret_price
    global burret_plus
    global end
    global check
    global check_barret
    counter -= barret_price
    while True:
        if (check == True):
            break
        counter += barret_plus
        Calculate(event = None)
        time.sleep(1)
def buy_barret():
    global barret_plus
    global counter
    global barret_price
    global check_barret
    if (counter < barret_price):
        return
    else:
        check_barret = True
        if (barret_plus == 1):
            barret_plus += 4
            Thread(target=BuyBarret).start()
        else:
            counter -= barret_price
            barret_plus += 1
def quit():
    global check
    check = True
    sys.exit()
def f():
    global check
    check = True
    sys.exit()
def EndGame():
    global counter
    global end
    global check_gun
    global check
    global check_rifle
    if (counter < end) or (check_gun == False) or (check_barret == False) or (check_vest == False) or (check_rifle == False):
        return
    else:
        counter -= end
        window = Tk()
        window.title("Congratulations!")
        window.geometry('800x640+0+0')
        l = Label(window, text = "Finally, you funeraled capitan Price", font=("Helvetica", 20), fg = 'black')
        b = Button(window, text = "F", font = ("Times", 60, 'bold'), fg = 'red', command = f)
        l.place(x = 70, y = 0)
        b.place(x = 100, y = 100)
def wait():
    time.sleep(5)
def vest():
    Thread(target=buy_vest).start()
def buy_vest():
    global plus
    global barret_plus
    global counter
    global check_vest
    if (counter < vest_price):
        return
    counter -= vest_price
    check_vest = True
    t1 = plus
    plus *= 2
    t2 = barret_plus
    barret_plus *= 2
    time.sleep(10)
    plus -= t1
    barret_plus -= t2
    return
def rifle():
    global counter
    global rifle_price
    global check_rifle
    global plus
    if (counter < rifle_price):
        return
    else:
        check_rifle = True
        counter -= rifle_price
        plus *= 2
def Tutorial():
    t_w = Tk()
    t_w.title("Tutorial")
    t_w.geometry('600x400+50+50')
    t_l = Label(t_w, text = "Respect gun gives you +10 score per click for each purchase;" + '\n' +
                            "Respect barret gives five score per second for each purchase;" + '\n' +
                            "Respect bulletproof vest activates double score bonus for each previous perchase for 10 seconds;" +
                            '\n' + "Respect rifle magnifies respects per click twice;" +
                            '\n' + "To win, you neeed to collect all capitan equipment, get 100000 respects and also end the funeral.",
                font = ("Times", 15)
                )
    t_l.pack()
GunButton = Button(text = "buy respect gun: " + str(gun_price),
            bg = 'black', fg = 'green', font = ('Times', '25', 'bold'), command = buy_gun,
            )
BarretButton = Button(text = "buy respect barret: " + str(barret_price),
            bg='black', fg='green', font=('Times', '25', 'bold'), command = buy_barret,
            )
VestButton = Button(text = "buy respect bulletproof vest: " + str(vest_price),
                      bg='black', fg='green', font=('Times', '19', 'bold'), command=vest,
                      )
WinButton = Button(text = "End cap's funeral (1000000 respects needed)", bg = 'black', fg = 'yellow', font=('Times', '25', 'bold'), command = EndGame)
TutorialButton = Button(text = "Tutorial", bg = 'grey', fg = 'white', font = ('Times', '11'), command = Tutorial)
Quit = Button(text = "Quit", bg = 'grey', fg = 'white', font = ('Times', '17'), command = quit)
Heavy = Button(text = "buy respect rifle: " + str(rifle_price),
                 bg='black', fg='green', font=('Times', '16', 'bold'), command=rifle,
               )
root.bind("<space>", Plus)
GunButton.place(x = 0, y = 180)
BarretButton.place(x = 0, y = 245)
TutorialButton.place(x = 0, y = 150)
VestButton.place(x = 0, y = 302)
Quit.place(x = 55, y = 134)
Heavy.place(x = 0, y = 353)
WinButton.pack()
text.pack()
root.mainloop()