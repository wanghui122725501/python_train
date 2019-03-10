class Person:
	def __init__(self):
		print("test")

p = Person()
print(type(p))


class Ma(object):
	def run(self):
		print("Ma zai run!")

	def eat(self):
		print("ma zai chi cao")

class Lv(object):
	def lamo(self):
		print("Lv zai lamo!")

	def eat(self):
		print("Lv zai chi cao!")

class Luozi(Ma,Lv):
	def eat(self):
		Lv.eat(self)    #如果不想按照MRO的方式执行，可以这样执行
		print("luozi zai chi daogu!")

L = Luozi()
print(Luozi.__mro__)    #查看调用方法顺序
# L.run()
# L.lamo()
L.eat()