s = '-045'

li =[]
set_1 = ('+','-',)
n=0
nmber=0
str_opr=""
for i in s:
    if i in set_1 and n==0:
        str_opr+=i
        n=i
    elif i==" ":
        break
    elif (48<= ord(i) <= 57):
       li.append(i)
       nmber =int (nmber*10 +int(i)) 
       n=1
    else :
        break

# nmber=int(str(nmber))
# nmber=str(nmber)

print(nmber)
str_opr=str_opr+str(nmber)

print(int(str_opr))

# print(li) 
# print(nmber)
# print(int (s))


# s="10"
# r="-"
# q=r+s
# print(int(q))