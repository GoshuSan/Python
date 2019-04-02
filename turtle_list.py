import turtle as t
dist=42
degree=90
print("f go forward, b go back in this program there's a lack, l go left and r go right guide the turtle and follow the light('f','b','r','l')")
moves=input()

for move in moves:   
    if move=='f':  
        t.forward(dist)
    elif move=='r':
        t.right(degree)
        t.forward(dist)
    elif move=='l':
        t.left(degree)
        t.forward(dist)
    elif move=='b':
        t.back(dist)
    else:
        print("Man plz stop kidding me, insert something usefull") 
        
t.end_fill()    
t.done()       