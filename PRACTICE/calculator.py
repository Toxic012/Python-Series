print("select cases")
print("1.ADD \n 2.Substract\n 3. division \n 4.multiplication")
n,m=map(int,input("enter two number using tab : ").split())
cases =  int (input("enter the case : "))

while (cases!=-1):
    if cases==1:
        print(n+m)
    elif cases==2:
        print(n-m)
    elif cases==3:
        print(n/m)
    elif cases==4:
        print(n*m)
    else :
        cases=-1
    

        