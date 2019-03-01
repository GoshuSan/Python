import turtle as t
n1=1
n2=1
ris=0
j=0
zoom=10

print("Numero della sequenza di Fibonacci da disegnare")
moves=input()
t.color('red')
while j in range(int(moves)):
    ris=n1+n2
    n1=n2
    n2=ris
    t.fd(n2*zoom)
    t.lt(90)
    t.fd(ris*zoom)
    t.lt(90)
    j+=1
t.done()


