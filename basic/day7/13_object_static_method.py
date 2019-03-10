class Person(object):
	country = 'china'
	def eat(self):
		print('hello')

	@classmethod
	def greet(cls):
		cls.country = "Japan"
		# print("ccc")

	@staticmethod
	def st_md():
		Person.country = "India"
		print('xxooxxooxxx')

p1 = Person()
#实例方法
# p1.eat()
# Person.eat()#不能执行

#类方法
print(Person.country)
Person.greet()
p1.greet()
print(Person.country)
p1.st_md()
Person.st_md()