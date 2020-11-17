#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru intervalul de la 1 la n (n-este citit de la tastatură).
n=int(input('n='))
for i in range (0,n,2):
    print(i, end=',')
