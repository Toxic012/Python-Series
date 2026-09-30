a= [1,2]
b=[3,4]
c=a+b
c.sort()
# print(c)
l=len(c)
mid=int(l/2)
# print(c[mid-1],c[mid])
d=[]
if l%2==0:
    index_strt=c[mid-1]
    index_end=c[mid]
    d.append(index_strt)
    d.append(index_end)
    e=(d[0]+d[1])/2
else :
    d.append(c[mid])  
    
# e="{:.4f}".format(e)

# print(d)