import random as r
import turtle as t

k=0
zoom=10
step=1
t.color('red')

print("Inserire il numero di movimenti:")
moves=input()

for k in range(int(moves)):
    if(r.random()>0.5):
        t.lt(90)
    else:
        t.rt(90)

    t.fd(step*zoom)

t.done()