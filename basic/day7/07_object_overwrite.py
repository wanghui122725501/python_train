class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def eat(self):
		print("人在吃饭")

class Student(Person):
	'''
	1. 如果父类的方法不能满足子类的需求，那么可以重写这个方法，以后对象调用同名方法的时候，就只会执行子类的这个方法
	2. 虽然父类的方法不能完全满足子类的需求，但是父类方法的代码还是需要执行，那么可以通过super这个函数调用父类的方法
	3. super(Child_class_name,self).__init__(参数)
	'''
	def __init__(self,name,age):
		super(Student,self).__init__(name,age)
		print("学生初始化")

	def eat(self):
		print("学生在吃饭")

	def greet(self):
		print('my name is %s,my age is %d'%(self.name,self.age))

s = Student('xxx',13)
# s.eat()
s.greet()