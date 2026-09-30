s= "ab"
p= "a."
otstr= ".*"
n=0
bool_1=False
emstr=""

if len(s)==len(p):
    
    # for i in range (len(s)):
    #     if p[i]=='.' or p[i]==s[i] and n==0:
    #         emstr+=s[i]
    #         n=1
    #     elif p[i]=='.' or p[i]==s[i] and n==0:
    #         emstr+=s[i]
    #     elif (p[i]=='*' or p[i]!=s[i]) and (s[i] not in emstr):
    #         emstr+='b'
    for x in range(len(s)):
        if p[x]=='.':
            emstr+='a'
        elif p[x]=='*':
            emstr+='b'
        elif p[x]==s[x]:
            emstr+=s[x]
        
            
print(emstr) 
     