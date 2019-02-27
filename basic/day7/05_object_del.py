import sys

class Person(object):
	def __init__(self):
		self.name = "abcd"
		print("this del func")
		self.fp = open('xxx','w',encoding='utf-8')

	def greet(self):
		print('hello i am %s'%self.name)

	def write(self,message):
		self.fp.write(message)

	def __del__(self):
		print("这是析构函数！！")
		self.fp.close()

p = Person()
p.greet()
print(sys.getrefcount(p))
p.write('xxxx')