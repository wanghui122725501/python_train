
f = open('notex.md','r',encoding='utf-8')
'''
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
'''

'''
不能使用for循环去遍历readline方法
for line in f.readline():
	print(line)
f.close()
'''

while True:
	line = f.readline()
	if not line:
		break
	print(line)
f.close()

