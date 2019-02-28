class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def eat(self):
		print("人在吃饭!")

	def run(self):
		print("人在跑步！")

class Student(Person):
	pass

s = Student('wanghui',12)
s.eat()
s.run()
print(s.name)
print(s.age)