

person = {
	"name":"wxx",
	"age":20,
	"style":"wenjing"
}

def eat(person):
	print("i am %s,and eat %s"%(person['name']))

class Person(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def eat(self):
		print("i am %s,and %s years old"%(self.name,self.age))



class Car(object):
	def __init(self,brand,xinghao):
		self.brand = brand
		self.xinghao = xinghao

	def run(self):
		print("%s is %s is running"%(self.brand,self.xinghao))

p1 = Person()
p1.eat()

