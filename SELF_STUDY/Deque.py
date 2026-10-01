from collections import deque

ll = deque()

# Insert
ll.append(10)        # add at end
ll.appendleft(20)    # add at beginning
ll.insert(1, 30)     # insert at index (O(n))

# Remove
ll.pop()             # remove last
ll.popleft()         # remove first
ll.remove(10)        # remove first occurrence of value

# Access
print(ll[0])         # first element
print(ll[-1])        # last element
print(len(ll))       # size

# Others
ll.clear()           # remove all
