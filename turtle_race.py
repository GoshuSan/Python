import turtle as t
import random as r
wndSize = 400
print("How many turtles do you wanna use?")
n_turtles=input()
t.setup(wndSize, wndSize)
wndDivision = wndSize/(n_turtles+1)
l=[]
cont=(0-(wndSize/2))
t.speed(1)
for i in range(0, n_turtles-1):
    tartaruga=t.Turtle()
    tartaruga.penup()
    tartaruga.setx(0-(wndSize/2))
    tartaruga.sety(cont + wndDivision)
    
    ran=r.randrange(0,7)
    if ran==0:
        tartaruga.color("red")
    elif ran==1:
        tartaruga.color("yellow")
    elif ran==2:
        tartaruga.color("blue")
    elif ran== :
        tartaruga.color("orange")
    elif ran==4:
        tartaruga.color("purple")
    elif ran==5:
        tartaruga.color("green")
    elif ran==6:
        tartaruga.color("black")
    cont=cont + wndDivision
    l.append(tartaruga)
t.penup()
ran = r.randrange(0,7)
if ran == 0:
    t.color("red")
elif ran == 1:
    t.color("yellow")
elif ran == 2:
    t.color("blue")
elif ran == 3:
    t.color("orange")
elif ran == 4:
    t.color("purple")
elif ran == 5:
    t.color("green")
elif ran == 6:
    t.color("black")
t.setx(0-(wndSize/2))
t.sety(cont+wndDivision)
cont = cont + wndDivision
l.append(t)
uscita = True
while uscita:
    for tartaruga in l:
        tartaruga.forward(r.randrange(0,16))
        if tartaruga.xcor() > (wndSize/2):
            uscita = False
            print("turtle ")
            print(i+1)
            print("ha vinto!")
