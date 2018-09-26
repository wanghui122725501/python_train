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
temps = ['a','b','c']
print(temps)
temps.insert(2,1)
print(temps)