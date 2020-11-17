#Să se calculeze sumele: 
n = int(input('n='))
s1 = 0
s2 = 0
s5 = 0
s6 = 0
for i in range(1, n):
    s1+=i
    s2+=((i-1)*i)
    s5+=(i/(i+1))
    s6+=(20+i)
s3=1
a=1
for b in range(2, n):
    a*=b
    s3+=a
s4=0
for b in range(1, ((n * 10) + 1)):
    if (b%10==0):
        s4+=(b+2)
print('s1=', s1)
print('s2=', s2)
print('s3=', s3)
print('s4=', s4)
print('s5=', s5)
print('s6=', s6)
