class Person(object):
	def __init__(self,name):
		self.__name = name
		self._age = 12
	
	def greet(self):
		print("hello %s"%self.__name)

	def __run(self):
		print("base class is running")


class Student(Person):
	def greet(self):
		# print('hello my name is %s'%self.__name)
		print('my age is %d'%self._age)
		self.__run()

p1 = Person('xxoo')
p1.greet()

s1 = Student('ooxx')
s1.greet()