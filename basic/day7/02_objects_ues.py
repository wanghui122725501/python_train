class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def eat(self):
		print("吃蛋！")

p1 = Person('aaa',10)
p2 = Person('bbb',20)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
