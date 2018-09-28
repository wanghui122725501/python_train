#append:添加一个元素到列表之后
'''
temps = [1,2,3,4]
print(temps)
temps.append(10)
print(temps)
'''

# count:统计元素出现的次数
'''
temps = ["to","be","or","not","to","be"]
counts = temps.count("to")
print(counts)
'''

# extend：拓展列表
'''
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
'''

# index:获取元素第一个出现的位置
'''
temps = ["to","be","or","not","to","be"]
print(temps.index('to'))
'''

# insert:插入到某个位置
'''
temps = ['a','b','c']
print(temps)
temps.insert(2,1)
print(temps)
'''

# pop
'''
temps = [1,2,3,4]
value = temps.pop()
print(value)
print(temps)
'''

# remove:z只会移除第一个对应的值
'''
temps = [1,2,3,4,1,1,1]
temps.remove(1)
print(temps)
'''
# reverse:反转,
'''
temps = [1,2,3,4]
new_temps = temps[-1::-1]
temps.reverse()
print(new_temps)
print(temps)
'''

# sort:排序
'''
temps = [23,34,56,3,53,2]
temps.sort(reverse=True)   #从大到小
new_temps = sorted(temps)   #sorted不会修改元数据
print(new_temps)
print(temps)
'''

#del 根据下标删除元素
'''
temps = [1,2,3,4]
del temps[0]
print(temps)
'''

# in 存在性判断
'''
temps = ["apple","banana","pare"]
if "orange" in temps:
	print("oringe in temps")
else:
	print("False")
'''

# list 函数
temps = "hello world"
new_temps = list(temps)
print(new_temps)

