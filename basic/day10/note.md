# 迭代器
**判断一个对象是否可迭代**
- 可迭代对象

也就是可以用for循环遍历的对象，常见的可迭代对象有：str，list，tuple，dict，set以及生成器
使用`isinstance()`去判断是否是一个可迭代对象（iterable）,类中有`__iter__`方法的话也会返回一个迭代器对象

迭代器可以使我们访问集合的时候非常方便，可以通过for...in....去方便的访问，这就是用迭代器完成的

- 迭代器
1. 在Python2中，实现了`next`和`__iter__`方法，并且在这个方法中返回了对象，叫做迭代器对象
2. 在python3中，实现了实现了`__next__`和`__iter__`方法，并且在这个方法中返回了对象，叫做迭代器对象
3. 如果迭代器没有返回值了,那么应该在`__next__`方法中跑出一个StopIterationy异常 
4. 使用iter()方法获取可迭代对象

## 问题：
- 什么是可迭代对象：
> 1. 用来作甚的：用来给for...in遍历的
2. 支持的数据类型：list,string,set,tuple,生成器
3. 需要满足的条件： 需要一个`__iter__`的方法，并且这个方法要返回一个可迭代对象

- 什么是迭代器：
1. 用来做什么的：用来返回数据的，每次循环的时候都会调用迭代器的`__next__`方法，通过这个方法获取数据
2. 需要满足的条件：需要实现两个方法`__iter__`和`__next__`

- 栗子：
```
from collections import Iterable


class MyRangeIterator(object):
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.start < self.end:
			temp = self.start
			self.start += 1
			return temp
		else:
			raise StopIteration()

class MyRange(object):
	"""
	myrange是可迭代对象
	"""
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		"""返回可迭代对象"""
		return MyRangeIterator(self.start,self.end)


ret = MyRange(1,10)
for x in ret:
	print(x)
# ret_iterator = iter(ret)
# while True:
# 	try:
# 		x = ret_iterator.__next__()
# 		print(x)
# 	except StopIteration:
# 		break

print("="*30)
for y in ret:
	print(y)
```
如果将迭代器和可迭代对象两个身份都放在同一个对象中，这个可迭代对象只能被遍历一次
```
from collections import Iterable

class MyRange(object):
	"""
	myrange是可迭代对象
	"""
	def __init__(self,start,end):
		self.start = start
		self.end = end
		self.index = start

	def __iter__(self):
		"""返回可迭代对象"""
		return self

	def __next__(self):
		if self.start < self.end:
			temp = self.start
			self.start += 1
			return temp
		else:
			raise StopIteration()

my_range = MyRange(1,10)
for i in my_range:
	print(i)

print("="*30)

for y in my_range:
	print(y)
```

# 生成器
循环1到100亿的问题，如果采用range的方式就会导致程序崩溃，range会生成一个很大的列表。为了防止将大量数据给机器处理带来资源上的巨大消耗，就需要迭代器来将大量数据循环处理
- 原理：
生成器通过函数产生，如果在函数中出现了yield表达式，那么函数不在是一个简单的函数，而是一个生成器函数，yield一次返回一个结果，并且会冻结当前函数的状态哦

- 即是迭代器，又可迭代对象，只能被遍历一次

```
# num_list = [x for x in range(1,1000000000)]
# print(type(num_list))


ret = (x for x in range(1,100000000000))
for x in ret:
	print(x)
```
使用函数

```
def my_gen(start,end):
	index = start
	while index <= end:
		yield index
		index += 1

ret = my_gen(1,1000000000)
for x in ret:
	print(x)
```
## send方法
send和next方法类似，可以触发生成器的下一个yield，打比赛股send不仅仅能触发下一个yield，还能发送数据过去，作为yield表达式的值,不能给刚开始的生成器传递参数
- 也是用来触发代码，直到碰到`yield`表达式
- 如果使用send方法执行刚刚开始的生成器，那么应该传递None方法，不然的话都会报错
- 尽量不要在生成器中使用return，不然会触发`StopInterrator`报错
**send和nest的区别**
- send方法可以传递值给yield表达式，next不可以
- 在第一次传递生成器代码的时候，send函数必须要传一个None进去，而next可以不用传

### 生成器的小案例
