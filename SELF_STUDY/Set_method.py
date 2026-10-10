s1 = {1,2,3,4,8}
s3 = {5,6,7}
s2 = {1,3,89,45,2}

print("diffrence = ",s1.difference(s2))
print("isdisjoint = ",s1.isdisjoint(s2))
print("isdisjoint = ",s1.isdisjoint(s3))
print("discard = ",s1.discard(s2))
print("discard = ",s1.discard(s3))
print("union = ",s1.union(s2))
print("intersection = ",s1.intersection(s2))