# s=list(input())
# print(s[::-1])
# z=""
# t=z.join(s[::-1])
# print(t)

# s=input()
# con =int (s)
# str1=""
# c=0
# while (con!=0):
#     temp=con%10
#     if (temp%2!=0):
#         c+=1
#         str1=str1+str(temp)
    
        
#     con=int(con/10)
# print(str1[::-1])

s,r=list(input().split())
r=str(r)
z=s[0:2]
x=s[2:]
i=x+z
t=""
y=t.join(i)
print(y==r)
