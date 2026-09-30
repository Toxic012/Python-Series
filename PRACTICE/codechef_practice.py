# li = [45, 67, 89, 34, 90]

# # Check if all elements are greater than 33
# result = all(x > 33 for x in li)

# print("All numbers > 33:", result)
t= int (input())
ch = 0
def check (n,li):
    if n in li :
        n+=1
        return n
    else : 
        ch =1
        return ch
        
temp=0

for i in range(t):
    
    a,b= map (int,input().split())
    
    
    li = list(map(int,input().split()))
    n=b
    while (ch==1):
        temp = check (n,li)
        
        ch = temp
    print(abs(temp-b))
    
    
    

    
    