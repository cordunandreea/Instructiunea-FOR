n=int(input('n='))
a=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        a+=i
print(a)