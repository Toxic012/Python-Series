s= "hello"

t= "olpeh"
print(sorted(t))
print(sorted(s))
def anagaram(s,t):
    bo=False
    if len(s)==len(t):
        for i in range(len(s)):
            if s[i]==t[i]:
                bo =True
            else :
                return False   
            
    return bo
print(anagaram(s,t))