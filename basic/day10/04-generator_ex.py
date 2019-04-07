

# num_list = [x for x in range(1,1000000000)]
# print(type(num_list))


ret = (x for x in range(1,100000000000))
for x in ret:
	print(x)
