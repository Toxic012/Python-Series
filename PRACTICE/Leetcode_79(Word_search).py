# li =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word="ABCCED"

# coun=0
# i=0
# j=0

# while  j < len(word):
#     if word[j] in li[i]:
#         coun += 1
#         print(li[i], word[j])
#         li[i].remove(word[j])   # still modifies row
#         j += 1
#     else:
#         i += 1
#         if i==len(li):
#             i=0
#         continue

# if coun == len(word):
#     print(True)
# else:
#     print(False)

li=[-1,0,1,2]
n=int(len(li)/2)
print(li[n])