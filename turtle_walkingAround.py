import turtle as t
dist=42
degree=90

while True:   
    print("The are the commands to move your soldier, try to not die ('f','b','r','l')")
    print("(Pressing 's' you can stop your mission)")
    move=input()
    if(len(move))>1:
        print("Ehi, the soldier doesn't have a good memory, insert commands one by one!")
    elif move=='f':  
        t.forward(dist)
    elif move=='r':
        t.right(degree)
        t.forward(dist)
    elif move=='l':
        t.left(degree)
        t.forward(dist)
    elif move=='b':
        t.back(dist)
    elif move=='s':
        break
    else:
        print("Cmon man stop joking and insert something useful") 

t.screen.bye()