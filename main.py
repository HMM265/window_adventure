from tkinter import *

window = Tk()
window.resizable(False, False)

menu3 = Menu(window)
file3 = Menu(window,
            tearoff=1)

imgdoor = PhotoImage(file="images/r_door.png")
imghole = PhotoImage(file="images/r_hole2.png")
imgkey = PhotoImage(file="images/r_key.png")
imgsand = PhotoImage(file="images/r_sand.png")
imgcreep = PhotoImage(file="images/r_creepyguy.png")
imgcliff = PhotoImage(file="images/r_cliff.png")
imgfield = PhotoImage(file="images/r_field.png")
imgvendor = PhotoImage(file="images/vendor.png")
imglockbox = PhotoImage(file="images/r_lockedbox.png")
imgrubber = PhotoImage(file="images/r_rubberband.png")
imgdust = PhotoImage(file="images/r_dust cloud.png")
imgrman = PhotoImage(file="images/r_rubberbandman.png")
imgcata = PhotoImage(file="images/r_catapult.png")
imgdhall = PhotoImage(file="images/r_darkhall2.png")
imgdarkbed = PhotoImage(file="images/r_darkbed.png")
imgeyes = PhotoImage(file="images/r_eyes.png")
imgnosleep = PhotoImage(file="images/r_nosleep1.png")
imgbigbox = PhotoImage(file="images/r_biglockbox.png")
imgcreature = PhotoImage(file="images/creature in the dark.png")
imgdeath = PhotoImage(file="images/r_died.png")
imgmwebb = PhotoImage(file="images/r_mikewebb.png")
imgtrophy = PhotoImage(file="images/r_trophy.png")
imghand = PhotoImage(file="images/r_hand.png")
imgexit = PhotoImage(file="images/r_exit.png")
imgyou = PhotoImage(file="images/r_ityou.png")
invkey = PhotoImage(file="images/inv_key.png")
invsand = PhotoImage(file="images/inv_sand.png")
invbox = PhotoImage(file="images/inv_box.png")
invrubberbands = PhotoImage(file="images/inv_rubberbands.png")
invcatapult = PhotoImage(file="images/inv_catapult.png")


key = 0
sand = 0
rubberbands = 0
catapult = 0
lbox = 0

items = {key, sand, rubberbands, catapult}


def restart():
    global L
    global b1
    global b2
    global des1
    global key
    global sand
    global rubberbands
    global catapult
    global lbox
    key = 0
    sand = 0
    rubberbands = 0
    catapult = 0
    lbox = 0
    label.destroy()
    label2.destroy()
    label3.destroy()
    window.geometry("1000x500")
    window.title("Button Adventure - Wunderful map (Tm)")
    window.config(bg="#cfb56d")
    window.resizable(False, False)

    menu = Menu(window)
    file = Menu(window,
                tearoff=1)
    L = Label(window,
              font=("Times", 20),
              text="Wunderful Map (Tm)",
              fg="#d4ab31",
              bg="grey")

    L.pack(side=TOP)

    b1 = Button(window,
                image=imgdoor,
                command=door)

    b1.place(x=210, y=175)

    b2 = Button(window,
                image=imghole,
                command=end12)

    b2.place(x=600, y=195)

    des1 = Label(window,
                 text="You follow your map to a door and a hole, the door is a pretty nice door but it looks way better"
                      " when contrasted to the hole (someone left their hands)",
                 wraplength=600,
                 font=("SimSun", 10, "bold"),
                 fg="black",
                 bg="white")

    des1.pack(side=TOP)

    file.add_command(label='Backpack', command=inventory)
    menu.add_cascade(label='Inventory', menu=file)
    window.config(menu=menu)


def inventory():
    inv = Toplevel()
    inv.geometry("400x400")
    inv.config(bg="#939ec2")
    inv.resizable(False, False)
    label1 = Label(inv,
                   text="Every item you collect will show up here!",
                   font=("SimSun", 10, "bold"))
    label1.pack(side=TOP)
    if key == 1:
        label2 = Label(inv,
                       image=invkey)
        label2.pack(side=BOTTOM)
    if sand == 1:
        label3 = Label(inv,
                       image=invsand)
        label3.pack(side=BOTTOM)
    if rubberbands == 1:
        label4 = Label(inv,
                       image=invrubberbands)
        label4.pack(side=BOTTOM)
    if catapult == 1:
        label5 = Label(inv,
                       image=invcatapult)
        label5.pack(side=BOTTOM)
    if lbox == 1:
        label5 = Label(inv,
                       image=invbox)
        label5.pack(side=BOTTOM)
    if key == 0 and sand == 0 and rubberbands == 0 and catapult == 0 and lbox == 0:
        label2 = Label(inv,
                       text="You currently have no items")
        label2.pack(side=BOTTOM)
    button = Button(inv,
                    text="exit",
                    command=inv.destroy,
                    font=("Times",15),
                    height=1,
                    width=3,
                    fg="red",
                    bg="black")
    button.pack(side=TOP)

def prize():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    label.destroy()
    label2.destroy()
    label3.destroy()
    window.title("The Mike Webb")
    window.geometry("600x886")
    window.config(bg="black")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgmwebb, )
    label.place(x=0,y=0)

    label2 = Label(window,
                   text="All is welcome to Mike Webbisim",
                   wraplength=200,
                   fg="#aa42eb",
                   bg="black",
                   font=("Times", 17, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)

def end11():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    window.title("Sacrifice ending")
    window.geometry("500x720")
    window.config(bg="black")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgyou, )
    label.pack(side=BOTTOM)

    label2 = Label(window,
                   text="You realize that this is the moment. You pull out you catapult aim it at the creature, but you"
                        "failed to realize that you have nothing to use as ammo. Then it dawns on you that YOU are the "
                        "ammo you hop in flip the switch. And fly towards the creature and your vision goes dark."
                        "(This was all the evidence at the scene)",
                   wraplength=500,
                   fg="red",
                   bg="black",
                   font=("Times", 11, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def end10():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    window.title("Fled ending")
    window.geometry("300x800")
    window.config(bg="black")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgexit, )
    label.pack(side=BOTTOM)

    label2 = Label(window,
                   text="Unable to think of what to do you take out the box and hold it up to the creature. The"
                        " creature stares at you and then you feel the wind getting weaker. It walks up to you and"
                        " takes the box it's lost staring at the box you take this time to look around and see a "
                        'convenient exit sign near a door and you "getta outta here...aah"',
                   wraplength=300,
                   fg="#f0c74d",
                   bg="black",
                   font=("Times", 11, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def end9():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    window.title("Sanded ending")
    window.geometry("600x500")
    window.config(bg="black")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imghand, )
    label.pack(side=BOTTOM)

    label2 = Label(window,
                   text="You reach your hand into your pocket you feel a wave of emotions. You feel every other"
                        " timelines where you threw sand and it failed horribly. However this time..."
                        " it was no different."
                        " You tossed it at the creature but it just blew right back in your face. You start writhing on"
                        " the floor but you think to yourself (NO I wont go down like this!). You get back up but then "
                        "you are crushed by the weight of many tons of sand (Try to get up this time)",
                   wraplength=600,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def end8():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    window.title("Best ending")
    window.geometry("600x600")
    window.config(bg="white")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgtrophy, )
    label.pack(side=BOTTOM)

    label2 = Label(window,
                   text="You launched the box at the creature and it exploded with a blinding white light. When you"
                        " looked back the only thing that you saw in its place was a trophy. (YOU WON) Go to the "
                        "options to claim your prize.",
                   wraplength=600,
                   fg="green",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Prize',command=prize)
    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def end7():
    global label
    global label2
    global label3
    S7.destroy()
    L.destroy()
    window.title("Perished ending")
    window.geometry("420x400")
    window.config(bg="black")
    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgdeath)
    label.pack(side=BOTTOM)
    label2 = Label(window,
                   text="You accept your fate and perish instantly......yep.....you're dead.......I can't even make up"
                        " an excuse or make a reason why you may have survived.",
                   wraplength=300,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def FinalF():
    global S7
    des1.destroy()
    b1.destroy()
    b2.destroy()
    S7 = Toplevel()
    S7.resizable(False, False)
    S7.geometry("1500x1000")
    S7.title("The final fight")
    S7.config(bg="black")
    creature = Label(S7,
                     image=imgcreature)
    creature.place(x=400, y=200)
    label = Label(S7,
                  text="As you walk to the end of the hallway you feel the darkness getting stronger, until finally you"
                       " reach the end. (You feel like you found the source of everything). "
                       "You find the most horrifying "
                       "creature that you have every seen at the center of the room. "
                       "You stare into its eyes and they're soulless. You start to "
                       "feel a strong wind and think that you're going to blow away if you don't do something quick.",
                  font=("SimSun", 12, "bold"),
                  wraplength=1500)
    label.pack(side=TOP)
    if catapult == 1:
        button = Button(S7,
                        text="USE CONSTRUCT (requires catapult)",
                        height=5,
                        font=("System", 15),
                        command=end11,
                        state=ACTIVE,
                        bg="#e6aa20")
        button.place(x=1150, y=200)
    if catapult == 0:
        button = Button(S7,
                        text="USE CONSTRUCT (requires catapult)",
                        height=5,
                        font=("System", 15),
                        command=end11,
                        state=DISABLED)
        button.place(x=1150, y=200)
    if lbox == 1:
        button2 = Button(S7,
                         text="hold up box (requires box",
                         height=5,
                         font=("System", 15),
                         command=end10,
                         state=ACTIVE,
                         bg="#e6aa20")
        button2.place(x=30, y=200)
    if lbox == 0:
        button2 = Button(S7,
                         text="hold up box (requires box",
                         height=5,
                         font=("System", 15),
                         command=end10,
                         state=DISABLED)
        button2.place(x=30, y=200)
    if sand == 1:
        button3 = Button(S7,
                         text="Pocket sand 2!!! (requires sand)",
                         height=5,
                         font=("System", 15),
                         command=end9,
                         state=ACTIVE,
                         bg="#e6aa20")
        button3.place(x=1150, y=600)
    if sand == 0:
        button3 = Button(S7,
                         text="Pocket sand 2!!! (requires sand)",
                         height=5,
                         font=("System", 15),
                         command=end9,
                         state=DISABLED)
        button3.place(x=1150, y=600)
    if lbox == 1 and catapult == 1:
        button4 = Button(S7,
                         text="Launch the box (requires box and catapult)",
                         height=5,
                         font=("System", 15),
                         command=end8,
                         state=ACTIVE,
                         bg="#e6aa20")
        button4.place(x=30, y=600)
    if lbox == 0 or catapult == 0:
        button4 = Button(S7,
                         text="Launch the box (requires box and catapult)",
                         height=5,
                         font=("System", 15),
                         command=end8,
                         state=DISABLED)
        button4.place(x=30, y=600)
    button5 = Button(S7,
                     text="   Perish   ",
                     height=5,
                     font=("System", 21),
                     command=end7)
    button5.place(x=715, y=780)


def end4():
    global label
    global label2
    global label3
    des1.destroy()
    b1.destroy()
    b2.destroy()
    L.destroy()
    window.title("Sleep ending")
    window.geometry("600x600")

    label = Label(window,
                  image=imgeyes, )
    label.place(x=0, y=0)

    label2 = Label(window,
                   text="You decide that you have had enough of this adventure and lay down and go to sleep. However "
                        "you can't sleep...You open your eyes and see something staring back.",
                   wraplength=300,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    label3 = Label(window,
                   image=imgnosleep)
    label3.place(x=300, y=400)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def FinalP1():
    global des1
    global b1
    global b2
    S6.destroy()
    des1 = Label(window,
                 text="Now returning to your map you find that you are nearly at an end you just have a few choices"
                      " left to make. You walk until you find a house, with this being the only structure here you "
                      "enter. When you get inside you see a dark hallway and a nice looking bed. (you are kinda tired)",
                 wraplength=600,
                 font=("SimSun", 10, "bold"),
                 fg="black",
                 bg="white")
    des1.pack(side=TOP)

    b1 = Button(window,
                     image=imgdhall,
                     command=FinalF)
    b1.place(x=100, y=150)

    b2 = Button(window,
                 image=imgdarkbed,
                 command=end4)
    b2.place(x=600, y=165)


def cata():
    global S6
    global rubberbands
    global catapult
    catapult = +1
    rubberbands = 0
    S5.destroy()
    S6 = Toplevel()
    S6.resizable(False, False)
    S6.title("perfection")
    S6.geometry("400x400")
    S6.config(bg="light blue")

    label = Label(S6,
                  text="Finally, after years of engineering you make the perfect construct. You take your masterpiece "
                       "and follow your map.",
                  font=("SimSun", 10, "bold"),
                  wraplength=400)
    label.pack(side=TOP)

    label1 = Label(S6,
                   image=imgcata)
    label1.place(x=100, y=50)

    button = Button(S6,
                    text="Proceed",
                    height=5,
                    width=30,
                    command=FinalP1)
    button.pack(side=BOTTOM)


def end3():
    global label
    global label2
    global label3
    S5.destroy()
    L.destroy()
    window.title("Floinged ending")
    window.geometry("300x452")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgrman, )
    label.place(x=0, y=0)

    label2 = Label(window,
                   text="Why?......Why? You had no reason to choose this option...... Why? Floingit isn't even a word.",
                   wraplength=300,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def bands():
    global rubberbands
    global S5
    rubberbands = +1
    S4.destroy()
    S5 = Toplevel()
    S5.resizable(False, False)
    S5.title("rubber bands")
    S5.geometry("400x400")
    S5.config(bg="light blue")
    label = Label(S5,
                  text="You reach slowly for the rubber bands and just when you are in reach you snatch them all in one"
                       " swift motion. You stare into your hands looking at the rubber bands just for a moment. When "
                       "you look up, the vendor is gone. (You think of what to do with the rubber bands)",
                  font=("SimSun", 10, "bold"),
                  wraplength=400)
    label.pack(side=TOP)
    label1 = Label(S5,
                   image=imgrubber)
    label1.place(x=150, y=100)
    button = Button(S5,
                    text="FLOINGIT",
                    height=5,
                    width=20,
                    command=end3)
    button.place(x=30, y=300)
    button2 = Button(S5,
                     text="CONSTRUCT",
                     height=5,
                     width=20,
                     command=cata)
    button2.place(x=230, y=300)


def end5():
    global label
    global label2
    global label3
    global key
    key = 0
    S5.destroy()
    L.destroy()
    window.title("Horror ending")
    window.geometry("600x600")
    window.config(bg="white")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label2 = Label(window,
                   text="You couldn't resist, You use your key to open the box and what you find... I can't even show"
                        " you...Just know you wont be doing any more adventuring.",
                   wraplength=600,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def resist():
    global S6
    global lbox
    lbox = +1
    S5.destroy()
    S6 = Toplevel()
    S6.resizable(False, False)
    S6.title("NO")
    S6.geometry("400x400")
    S6.config(bg="#4f1907")
    label = Label(S6,
                  image=imgbigbox)
    label.place(x=100, y=100)
    label = Label(S6,
                  text="You snap to your senses and push yourself away from the box. As you look around you find that "
                       "whoever that one guy was is gone. You stare at the box and decide to take it because it may be"
                       " useful later.",
                  font=("SimSun", 10, "bold"),
                  wraplength=400)
    label.pack(side=TOP)

    button = Button(S6,
                    text="Collect box",
                    height=5,
                    width=20,
                    command=FinalP1)
    button.pack(side=BOTTOM)


def end6():
    global label
    global label2
    global label3
    S5.destroy()
    L.destroy()
    window.title("Insanity ending")
    window.geometry("400x400")
    window.config(bg="#4f1907")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgbigbox)
    label.place(x=100, y=120)

    label2 = Label(window,
                   text="You soon realize that you have no key to open the box. You soon think to yourself (no there "
                        "has to be a key) You would go search around but you wouldn't want to leave the box. Finally "
                        "you come to the conclusion that (If I wait here long enough it might open)...... it never did",
                   wraplength=400,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def box():
    global S5
    S4.destroy()
    S5 = Toplevel()
    S5.resizable(False, False)
    S5.title("lockbox")
    S5.geometry("400x400")
    S5.config(bg="#4f1907")
    label2 = Label(S5,
                   image=imgbigbox)
    label2.place(x=100, y=100)
    label = Label(S5,
                  text="You see the box and are mesmerized (you completely forget about the merchant) Everything around"
                       " you goes dark only the box is in sight. And you?",
                  font=("SimSun", 10, "bold"),
                  wraplength=400)
    label.pack(side=TOP)
    if key == 1:
        button = Button(S5,
                        text="OPEN THE BOX (use key)",
                        height=5,
                        width=20,
                        command=end5,
                        bg="#e6aa20")
        button.place(x=25, y=300)

        button2 = Button(S5,
                         text="IRON WILL (resist!)",
                         height=5,
                         width=20,
                         command=resist)
        button2.place(x=225, y=300)
    else:
        button = Button(S5,
                        text="OPEN THE BOX (requires key)",
                        height=5,
                        width=22,
                        command=end5,
                        state=DISABLED)
        button.place(x=25, y=300)
        button2 = Button(S5,
                         text="W-Wait where's the key?",
                         height=5,
                         width=20,
                         command=end6)
        button2.place(x=225, y=300)


def evil():
    global S6
    global sand
    global catapult
    global lbox
    lbox = +1
    catapult = +1
    sand = 0
    S4.destroy()
    S6 = Toplevel()
    S6.resizable(False, False)
    S6.title("you monster")
    S6.geometry("600x421")
    label = Label(S6,
                  image=imgdust)
    label.place(x=0, y=0)
    label1 = Label(S6,
                   text="You feel the sand in your pocket, and with an evil grin you throw the sand in the trader's"
                        " eyes. You then close your eyes so the sand doesn't get in your own eyes. When you open them"
                        " the trader is gone and the box and the rubber bands are laying on the ground. "
                        "you pay no mind to the items (you monster)",
                   font=("SimSun", 10, "bold"),
                   wraplength=600)
    label1.pack(side=TOP)

    button = Button(S6,
                    text="Take box and craft catapult",
                    command=FinalP1,
                    height=5,
                    width=20)
    button.pack(side=BOTTOM)


def vendor():
    global S4
    S3.destroy()
    S4 = Toplevel()
    S4.resizable(False, False)
    S4.title("vendor")
    S4.geometry("600x400")
    label = Label(S4,
                  image=imgfield)
    label.place(x=0, y=0)
    label2 = Label(S4,
                   image=imgvendor)
    label2.place(x=200, y=100)

    label3 = Label(S4,
                   text="After observing the surrounding area and using common sense you soon realise that the creepy"
                        " fella is actually a vendor and he offers you his wares(two items), you have a feeling that"
                        " you can only take one (Can you really trust him?)",
                   wraplength=600,
                   font=("SimSun", 10, "bold"))
    label3.pack(side=TOP)

    button1 = Button(S4,
                     image=imglockbox,
                     command=box)
    button1.place(x=130, y=200)

    button2 = Button(S4,
                     image=imgrubber,
                     command=bands)
    button2.place(x=370, y=150)

    if sand == 0:
        button3 = Button(S4,
                         text="Take both (you don't have sand)",
                         height=5,
                         width=25,
                         state=DISABLED)
        button3.place(x=300, y=300)
    if sand == 1:
        button3 = Button(S4,
                         text="Take both (requires sand)",
                         height=5,
                         width=20,
                         state=ACTIVE,
                         command=evil,
                         bg="#e6aa20")
        button3.place(x=300, y=300)


def end2():
    global label
    global label2
    global label3
    global sand
    sand = 0
    S3.destroy()
    L.destroy()
    window.title("Dust ending")
    window.geometry("600x421")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgdust, )
    label.place(x=0, y=0)

    label2 = Label(window,
                   text="After performing all of those flips you land on your feet and quickly pull out your sand and "
                        "throw it in the creature's eyes. However you are way to far away for the sand to reach but"
                        " just at that moment a gust of wind shows up and blows the sand in your eyes. "
                        "(you never recovered)",
                   wraplength=600,
                   fg="red",
                   bg="black",
                   font=("Times", 12, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def l10():
    global S3
    S2.destroy()
    S3 = Toplevel()
    S3.resizable(False, False)
    S3.title("landed")
    S3.geometry("600x400")
    label = Label(S3,
                  image=imgfield)
    label.place(x=0, y=0)

    label2 = Label(S3,
                   text="After using your acrobatic skills to get away you quickly spin around and?",
                   font=("SimSun", 10, "bold"))
    label2.pack(side=TOP)

    button = Button(S3,
                    text="Observe your surroundings",
                    height=5,
                    width=20,
                    command=vendor)
    button.place(x=50, y=300)

    if sand == 0:
        button2 = Button(S3,
                         text="POKET SAND! (requires sand)",
                         height=5,
                         width=23,
                         state=DISABLED)
        button2.place(x=400, y=300)
    if sand == 1:
        button2 = Button(S3,
                         text="POKET SAND (requires sand)",
                         height=5,
                         width=22,
                         state=ACTIVE,
                         command=end2,
                         bg="#e6aa20")
        button2.place(x=400, y=300)


def end1():
    global label
    global label2
    global label3
    S2.destroy()
    L.destroy()
    window.title("Cliff ending")
    window.geometry("900x600")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window,
                  image=imgcliff, )
    label.place(x=0, y=0)

    label2 = Label(window,
                   text="In your haste you didn't take the time to look at your surroundings and failed to notice"
                        " the massive cliff behind you. Hopefully you have a nice soft rock to cushion your fall.",
                   wraplength=800,
                   fg="red",
                   bg="black",
                   font=("Times", 15, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def acrobatics():
    global S2
    Opt2.destroy()
    S2 = Toplevel()
    S2.resizable(False, False)
    S2.title("quick!")
    S2.geometry("600x400")
    S2.config(bg="#f79cbc")
    label1 = Label(S2,
                   text="You quickly flip on your feet and your only hope is to perform a series of back flips",
                   font=("SimSun", 10, "bold"),
                   wraplength=600)
    label1.pack(side=TOP)

    button1 = Button(S2,
                     text="perform 5 backflips",
                     height=5,
                     width=20,
                     bg="#0b702f",
                     fg="#eaed0e",
                     command=l10)
    button1.place(x=20, y=300)

    button2 = Button(S2,
                     text="perform 10 backflips",
                     height=5,
                     width=20,
                     bg="#0b702f",
                     fg="#eaed0e",
                     command=l10)
    button2.place(x=225, y=300)

    button3 = Button(S2,
                     text="Perform 99 backflips",
                     height=5,
                     width=20,
                     bg="#0b702f",
                     fg="#eaed0e",
                     command=end1)
    button3.place(x=430, y=300)


def Scene2P1():
    global Opt2
    C1.destroy()
    Opt2 = Toplevel()
    Opt2.resizable(False, False)
    Opt2.title("as you wake up")
    Opt2.geometry("400x400")
    Opt2.config(bg="#f25757")
    label1 = Label(Opt2,
                   font=("SimSun", 10, "bold"),
                   text="As you wake up you see a cheeky looking man staring at you with a smile",
                   wraplength=400)
    label1.pack(side=TOP)

    button1 = Button(Opt2,
                     height=5,
                     width=30,
                     text="ACROBATICS",
                     command=acrobatics)
    button1.pack(side=BOTTOM)

    creep = Label(Opt2,
                  image=imgcreep)
    creep.pack()


def keyfunc():
    global key
    global C1
    key = + 1
    Opt1.destroy()
    C1 = Toplevel()
    C1.resizable(False, False)
    C1.title("consequences")
    C1.geometry("400x400")
    C1.config(bg="black")
    label1 = Label(C1,
                   text="After you pick up the key the wind overpowers you and you fly out the room, your vision "
                        "goes dark",
                   font=("SimSun", 10, "bold"),
                   wraplength=400)
    label1.pack(side=TOP)
    end1 = Button(C1,
                  height=5,
                  width=30,
                  text="Proceed",
                  command=Scene2P1)
    end1.pack(side=BOTTOM)


def sandfunc():
    global sand
    global C1
    sand = + 1
    Opt2.destroy()
    C1 = Toplevel()
    C1.resizable(False, False)
    C1.title("consequences")
    C1.geometry("400x400")
    C1.config(bg="black")
    label1 = Label(C1,
                   text="After you get a handful of sand the wind blows away the rest of the sand and then "
                        "overpowers you and you fly out the room, your vision goes dark",
                   font=("SimSun", 10, "bold"),
                   wraplength=400)
    label1.pack(side=TOP)
    end = Button(C1,
                 height=5,
                 width=30,
                 text="Proceed",
                 command=Scene2P1)
    end.pack(side=BOTTOM)


def keyd():
    global Opt1
    Ph1.destroy()
    Opt1 = Toplevel()
    Opt1.resizable(False, False)
    Opt1.title("The key")
    Opt1.config(bg="black")
    Opt1.geometry("400x400")

    label = Label(Opt1,
                  text="As you go to pick up your key the sand behind you blows away (you honestly don't care)",
                  wraplength=400,
                  font=("SimSun", 10, "bold"))
    label.pack(side=TOP)
    keyb = Button(Opt1,
                  text="Collect",
                  height=5,
                  width=30,
                  command=keyfunc)
    keyb.pack(side=BOTTOM)


def sandd():
    global Opt2
    Ph1.destroy()
    Opt2 = Toplevel()
    Opt2.resizable(False, False)
    Opt2.title("sand?")
    Opt2.config(bg="black")
    Opt2.geometry("400x400")

    label = Label(Opt2,
                  text="As you go to take some sand the key behind you flies away into a dark corner in the room "
                       "(This saddens you deeply)",
                  wraplength=400,
                  font=("SimSun", 10, "bold"))
    label.pack(side=TOP)
    sandb = Button(Opt2,
                   text="Collect",
                   height=5,
                   width=30,
                   command=sandfunc)
    sandb.pack(side=BOTTOM)


def end12():
    global label
    global label2
    global label3
    L.destroy()
    b1.destroy()
    b2.destroy()
    des1.destroy()
    window.title("Rushed ending")
    window.geometry("600x600")
    window.config(bg="black")

    label3 = Label(window)
    label3.place(x=0, y=0)
    label = Label(window, )
    label.place(x=0, y=0)
    label2 = Label(window,
                   text="You know this would be a really cool path that led to more stuff, but I don't got time for "
                        "that so you get this really bad ending that sucks. I honestly don't know why you are even"
                        " reading this. Lets just say that the hole was actually a picture on the floor. So just press"
                        " the restart button in the menu and just pick the door.",
                   wraplength=600,
                   fg="red",
                   bg="black",
                   font=("Times", 15, "bold"))
    label2.pack(side=TOP)

    menu2 = Menu(window)
    file2 = Menu(window,
                 tearoff=1)

    file2.add_command(label='Inventory', command=inventory)
    file2.add_command(label='Restart', command=restart)
    file2.add_command(label='Exit', command=exit)
    menu2.add_cascade(label='Game Options', menu=file2)
    window.config(menu=menu2)


def door():
    global Ph1
    Ph1 = Toplevel()
    Ph1.resizable(False, False)
    Ph1.geometry("900x400")
    Ph1.title("What you found inside was")
    Ph1.config(bg="#696258")
    b1.destroy()
    b2.destroy()
    des1.destroy()
    pb1 = Button(Ph1,
                 image=imgkey,
                 command=keyd, )
    pb1.pack(side=LEFT)
    pb2 = Button(Ph1,
                 image=imgsand,
                 command=sandd)
    pb2.pack(side=RIGHT)
    pdes1 = Label(Ph1,
                  text="you walk in and find a dark cold room (you honestly expected better from how nice the door was),"
                       "as you go further in you find a nice juicy key on one side and on the other you find a pile of "
                       "sand. However a gust of wind blows from nowhere and you can only grab one of the items.(PICK ONE)",
                  font=("SimSun", 10, "bold"),
                  fg="black",
                  bg="white",
                  wraplength=400)
    pdes1.pack(side=TOP)

def start():
    menu = Menu(window)
    file = Menu(window,
                tearoff=1)
    global L
    global b1
    global b2
    global des1

    L.destroy()
    label.destroy()
    b1.destroy()
    label2.destroy()

    window.attributes('-fullscreen', False)
    window.geometry("1000x500")
    window.title("Button Adventure - Wunderful map (Tm)")
    window.config(bg="#cfb56d")
    window.resizable(False, False)

    L = Label(window,
              font=("Times", 20),
              text="Wunderful Map (Tm)",
              fg="#d4ab31",
              bg="grey")

    L.pack(side=TOP)

    b1 = Button(window,
                image=imgdoor,
                command=door)

    b1.place(x=210, y=175)

    b2 = Button(window,
                image=imghole,
                command=end12)

    b2.place(x=600, y=195)

    des1 = Label(window,
                 text="You follow your map to a door and a hole, the door is a pretty nice door but it looks way better"
                      " when contrasted to the hole (someone left their hands)",
                 wraplength=600,
                 font=("SimSun", 10, "bold"),
                 fg="black",
                 bg="white")

    des1.pack(side=TOP)

    file.add_command(label='Backpack', command=inventory)
    menu.add_cascade(label='Inventory', menu=file)
    window.config(menu=menu)


window.title("Window Adventure")
window.geometry("1500x800")
window.config(bg="#fcf5cc")
L=Label(window,
        font=("Times", 50),
        text="Window Adventure",
        fg="#d4ab31",
        bg="#3b473e")
L.pack(side=TOP)
b1 = Button(window,
            text="Start",
            font=("Times",30),
            height=2,
            width=20,
            command=start,)
b1.place(x=525,y=300)
label = Label(window,
              text="This is the DESCRIPTION of the game. The windows and toplevels are supposed to be the size that"
                   " they are. At the start of the game you follow your map to two choices and have to decide where"
                   " to go. As you play you can collect items that let you access other options. (You can see these"
                   " items in the inventory in the top left when you start) There are 12 endings, can you find them"
                   " all?",
              wraplength=1000,
              font=("Times",20),
              fg="red",
              bg="black")
label.pack(side=BOTTOM)
label2 = Label(window,
               text="by Ayden Daugherty",
               height=2,
               width=20,
               font=("SimSun",15),
               fg="#f7bb14",
               bg="black")
label2.place(x=650,y=440)
file3.add_command(label='Are you sure?', command=exit)
menu3.add_cascade(label='Exit', menu=file3)
window.config(menu=menu3)

window.mainloop()
