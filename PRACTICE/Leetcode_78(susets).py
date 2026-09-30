li=[[]]
nums=[1,2,3]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        # li.append(nums[:j])
        # li.append(nums[i:j])
        temp=[j]
        li.append(temp)
        li.append(nums[i:j])

print(li)