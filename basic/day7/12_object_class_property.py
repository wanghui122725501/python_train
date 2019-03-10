class Person(object):
	country = 'china' 
	def __init__(self,name):
		self.name = name

	def greet(self):
		print('my name is %s,my country is %s'%(self.name,self.country))
		# print('my name is %s,my country is %s'%(self.name,country))  不能这样写

'''
p1 = Person('xx')
p1.age = 12
print(p1.name)

p2 = Person('xxoo')
# print(p2.age) #报错
print(p2.name)
'''

p1 = Person('alex')
print(p1.country)
p1.country = 'xxxooooo'
print(p1.country)
print(Person.country)
p2 = Person('wanghui')
p2.country = "aaa"
print(p2.country)
print(Person.country)

## 修改类属性的正确姿势
Person.country = "Japan"
print(Person.country)

p1.greet()
p2.greet()