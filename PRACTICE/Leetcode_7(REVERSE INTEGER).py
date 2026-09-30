a = -120
um=0
if a<0:
    a=a*-1
    while (a!=0):
        um=(um*10+a%10)
        a=int(a/10)
    print(-um)
else:
    while (a!=0):
        um=(um*10+a%10)
        a=int(a/10)
    print(um)
