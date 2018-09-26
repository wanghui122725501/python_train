# 嵌套列表
# a = [1,2,3,"a",2.3]
# print(a)

# 嵌套列表的遍历
'''
a = [1,2,3,["a","b","c"]]
for x in a:
	if type(x) == list:
		for y in x:
			print(y)
	else:
		print(x)
'''

# 相加
'''
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
'''

# 切片操作
a = [1,2,3,4,5,6,7,8,9]
b = a[0:3]
c = a[0::2]    #带步长的奇数，
d = a[-1:-4:-1]  #逆序操作
e = a[-1::-1]    #全部逆序
print(b)
print(c)
print(d)
print(e)