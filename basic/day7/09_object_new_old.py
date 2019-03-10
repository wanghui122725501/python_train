class Person:
	def __init__(self,name):
		self.name = name

class Student(Person):
	def __init__(self,name):
		# super(Student,self).__init__(name)
		print("this is child class")
		Person.__init__(self,name)   #旧式类的调用

s1 = Student('xxx')
print(s1.name)
print(type(s1))
print(s1.__class__)