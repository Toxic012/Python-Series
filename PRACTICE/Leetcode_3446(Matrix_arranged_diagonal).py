A =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(len(li))
# li_mid=[]
# li_upper=[]
# li_down=[]


# for i in range(len(li)):
#     for j in range(len(li)):
#         if i==j:
#             li_mid.append(li[i][j])
#         elif i<j:
#             li_upper.append(li[i][j])
#         else:
#             li_down.append(li[i][j])

# print(li_upper,li_mid,li_down)    


n = len(A)
all_diagonals = []

# Upper diagonals (including main)
for k in range(n):
    for i in range(n-k):
        all_diagonals.append(A[i][i+k])

# Lower diagonals (below main)
for k in range(1, n):
    for i in range(n-k):
        all_diagonals.append(A[i+k][i])

# Sort them
sorted_diagonals = sorted(all_diagonals)

print("All diagonal elements:", all_diagonals)
print("Sorted diagonal elements:", sorted_diagonals)