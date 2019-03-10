# class Person(object):
# 	def eat(self):
# 		pass

# class Student(Person):
# 	def eat(self):
# 		pass

# class Teacher(Person):
# 	def eat(self):
# 		pass

# def greet(Pseron p):
# 	p.eat()

# p1 = Student()
# greet(p1)

# p2 = Person()
# greet(p2)


class Hero(object):
	def __init__(self):
		pass

	def stroke(self):
		pass

class Chengyaojin(Hero):
	def stroke(self):
		print("Chengyaojin DDDDDD")

class Xiangyu(Hero):
	def stroke(self):
		print("Xiangyu XXXX")

value = input("choose your hero").strip()
hero = None
if value == '1':
	hero = Chengyaojin()
else:
	hero = Xiangyu()

hero.stroke()
