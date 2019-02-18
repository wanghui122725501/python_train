a = [1,2,3,4,5,6,7,8]


# filter
b = filter(lambda x:True if x > 3 else False,a)
c = filter(lambda x:x>3,a)
for x in c:
	print(x)

# map
d = map(lambda x:x*10,a)
for i in d:
	print(i)
from functools import reduce
# reduce
e = reduce(lambda x,y:x+y ,a)
print(e)