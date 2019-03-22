#!/usr/bin/python3
from pygame import mixer
import os,random
import webbrowser
import datetime
import turtle
import math
import random
from playsound import playsound
min = 1
max = 6
i=1

from subprocess import call
import vlc




start_= random.randint(1,3)
start={1:"Hi !",2:"Hello, How are you ?",3:"Greetings"}
call(["espeak",start[start_]])
now = datetime.datetime.now()

print('''1: say,
        2: web,
        3: today,
        4: wiki,
        5: background,
        6: game,
        7:sound,
        8:music''')



Liam_fulla=r"hihowareyou.mp3"
Liam_hi=r"hi.mp3"
Liam_how=r"how.mp3"
Liam_are=r"are.mp3"
Liam_you=r"you.mp3"
jajoya=r"jajoy2.mp3"
johnnya=r"johndepp.mp3"
hpa=r"hp.mp3"
anakina=r"anakin.mp3"
jaune=r"jaune.mp3"
nani=r"nani.mp3"
deus=r"deus.mp3"
vult=r"vult.mp3"
slav=r"slav.mp3"
sax=r"sax.mp3"
gandalf=r"gandalf.mp3"
pirate=r"pirate.mp3"
nine=r"nine.mp3"
niness=r"90s.mp3"
cristina=r"cristina.mp3"
song1=r"Carve_our_name.mp3"
elise=r"elise.mp3"
brave=r"Brave.mp3"
silence=r"silence.mp3"
moonlight=r"Moonlight.mp3"
def sound():
    def nineties():
        playsound(niness)
        
        return



    def nnie():
        playsound(nine)
        
        return

    def nanni():
        playsound(nani)
        
        return
    def vultt():
        playsound(vult)
        
        return 
    def deus_vult():
        playsound(deus)
        
        return 

    def Liam_full():
        playsound(Liam_fulla)
        
        return
    def jaunea():
        playsound(jaune)
        
        return 
    def jajoy():
        playsound(jajoya)
        
        return 
    def johnny():
        playsound(johnnya)
        
        return 

    def hp():
        playsound(hpa)
        
        return 
    def anakin():
        playsound(anakina)
        
        return 
    def slave():
        playsound(slav)
        
        return
    def saxx():
        playsound(sax)
        
        return
    def gandalff():
        playsound(gandalf)
        
        return
    def piratte():
        playsound(pirate)
        
        return
    def cristinaa():
        playsound(cristina)
        
        return 
    switcher = {
            1: Liam_full,
            2: jajoy,
            3: johnny,
            4: hp,
            5: anakin,
            6: jaunea,
            7: nanni,
            8: deus_vult,
            9: vultt,
            10: slave,
            11: saxx,
            12: gandalff,
            13: piratte,
            14: nnie,
            15: nineties,
            16: cristinaa
        }
     
    def commande(n):
        
        # Get the function from switcher dictionary
        func = switcher.get(n, "nothing")
        # Execute the function
        return func()
        
    
    okt=int(input("        enter "))

    commande(okt)
        

def music():
         
    switcher = {
           1: song1,
           2: elise,
           3: brave,
           4: silence,
           5: moonlight
        }
     
    print('''1: Carve our name,
           2:  For elise,
           3: We are the brave,
           4: Somg of silence,
           5: Moonlight Sonata''')
    
    comm=int(input("enter "))

    func = switcher.get(comm, "nothing")
    if comm ==1:
        nom="Carve our name"
    elif comm==2:
        nom ="For Elise"
    elif comm==3:
        nom =" We are the Brave"
    elif comm == 4:
        nom="Song of Silence"
    elif comm==5:
        nom="Moonlight sonata"
    else:
        comm=5
    gg1_= random.randint(1,2)
    gg1={1:"Ready to sing"+nom,2:"Oh yeah i love this song"}
    call(["espeak",gg1[gg1_]])
    playsound(switcher[comm])
    info="do you want some info on this song ?"
    call(["espeak",info])
    userr= input("?")
    if userr=="yes":
        nom=nom.replace(" ", "_")
        nom=nom.lower()
        webbrowser.open('https://en.wikipedia.org/wiki/'+nom)
    else:
        rep="ok whatever ?"
        call(["espeak",rep])
    return

def say():
    gg1_= random.randint(1,3)
    gg1={1:"what did i must say ?",2:"I feel the sudden urge to say",3:"Hey you know what apparently i'm a Parrot so here we go"}
    call(["espeak",gg1[gg1_]])
    phrase= input("sentence ?\n")
    gg=str(phrase)
    call(["espeak",gg])
    
    return 
 
def web():
    g_= random.randint(1,3)
    g={1:"Where dou you want to go ?",2:"You have the most impresive database and you choose this one how dissapointing",3:"Here we go !"}
    call(["espeak",g[g_]])
    
    w = input("address ?\n")
    return webbrowser.open('http://'+w+'.ie')
 
def today():
    day = datetime.date.today().strftime('%A')
    month = datetime.date.today().strftime('%B')
    date = datetime.date.today().strftime('%d')
    g="Today is"+day+date+month
    call(["espeak",g])
    return str(now)
 
def wiki():
    g_= random.randint(1,3)
    g={1:"What do you want to know ?",2:"Wikipedia really ?",3:"As you wish !"}
    call(["espeak",g[g_]])
    w = input("subject ?\n")
    w=w.replace(" ", "_")
    w=w.lower()
    webbrowser.open('https://en.wikipedia.org/wiki/'+w)
    return
 
def background():
   x=random.randint(1,4)
   image = {1:r"t.gif",2:r"o.gif",3:r"y.gif",4:r"u.gif"}
   screen = turtle.Screen()

   screen.addshape(image[x])
   turtle.shape(image[x])
   turtle.exitonclick()
   print(x)
    
   return 
 
def game():
    
    print ("Rolling the dices...")
        
    print ("The values are....")
    a=(random.randint(min, max))
    print(a)
        
    b=(random.randint(min, max))
    print(b)
        
        
    return ""

switcher = {
        1: say,
        2: web,
        3: today,
        4: wiki,
        5: background,
        6: game,
        7: sound,
        8: music
    }
 
def commande(n):
    
    # Get the function from switcher dictionary
    func = switcher.get(n, "nothing")
    # Execute the function
    return func()
    

u=0
o=1
pre =0
previous=0
while u!=o:
    if previous==0:
        okt=int(input("enter "))
        previous=1
        previous_str=switcher[okt]
        ssp_= random.randint(1,3)
        ssp={1:"I will execute your command",2:"Alright master",3:"As you wish !"}
        call(["espeak",ssp[ssp_]])
        g="execution of function number"+str(okt)
        call(["espeak",g])
        commande(okt)
    elif previous == 1 :
        okt=int(input("enter "))
        if previous_str == switcher[okt]:
            pre += 1
            ssp_= random.randint(1,3)
            ssp={1:"I will execute your command again",2:"You know i can do something else",3:"How imaginative "}
            call(["espeak",ssp[ssp_]])
            commande(okt)
        else:
            previous_str=switcher[okt]
            ssp_= random.randint(1,3)
            ssp={1:"I will execute your command",2:"Alright master",3:"As you wish !"}
            call(["espeak",ssp[ssp_]])
            g="execution of function number"+str(okt)
            call(["espeak",g])
            previous=0
            commande(okt)
    else:
        previous=0
