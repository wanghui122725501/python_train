from collections import Iterable,Iterator

ret = isinstance([1,2,3],Iterable)
print(ret)

ret1 = isinstance("123",Iterable)
print(ret)

ret2 = isinstance(123,Iterable)
print(ret2)


class My_iter(object):
	def __iter__(self):
		pass

ret3 = My_iter()
print(isinstance(ret3,Iterable))

class MyRange(object):
	def __iter__(self):
		pass

	def __next__(self):
		pass

ret4 = MyRange()
print(isinstance(ret4,Iterator))