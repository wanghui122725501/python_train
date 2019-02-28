# 面向对象
[toc]
## 简介
面向对象：
    - 思考方式：
面向过程：

## 类和对象的使用
```
class Person(object):

	def eat(self):
		print("吃蛋！")

p1 = Person()
p1.eat()
```
## 访问限制
- 受保护的属性和方法:万不得已可以调用
```
class Woman(object):

	def __init__(self,age):
		self._age = age


w = Woman(13)
print(w._age)
```
- 私有属性和方法：不能被调用
```
class Account(object):
	def __init__(self,id,passwd):
		self.id = id
		self.__passwd = passwd

	def __account_list(self):
		print("我是私有方法")
		return [11,22,33]

	def get_account_list(self,passwd):
		if passwd == self.__passwd:
			return self.__account_list()

		else:
			return None

a1 = Account('aaa','123456')
a1.get_account_list('123456')
print(a1._Account__passwd)   #调用私有属性的方法
```

## 析构函数
也就是`__del__`方法，内存即将被收回的事后调用,文甲流的关闭和数据的释放

## 引用计数
sys.getrefcount(obj)  #临时变量的说法

## 继承
```
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
```

## 重写父类的方法
1. 如果父类的方法不能满足子类的需求，那么可以重写这个方法，以后对象调用同名方法的时候，就只会执行子类的这个方法
2. 虽然父类的方法不能完全满足子类的需求，但是父类方法的代码还是需要执行，那么可以通过super这个函数调用父类的方法
3. super(Child_class_name,self).__init__(参数)
```
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
```
4. 父类中的私有变量(方法)不能在子类中使用，受保护的可以使用


```
class Person(object):
	def __init__(self,name):
		self.__name = name
		self._age = 12
	
	def greet(self):
		print("hello %s"%self.__name)


class Student(Person):
	def greet(self):
		# print('hello my name is %s'%self.__name)
		print('my age is %d'%self._age)

p1 = Person('xxoo')
p1.greet()

s1 = Student('ooxx')
s1.greet()
```

## 新式类与旧式类
有没有指定任何父类的是`旧式类`
1. 如果父类是旧式类，子类的话也是旧式类
2. 在旧式类中不能使用super来调用父类的函数
```
class Person:
	def __init__(self,name):
		self.name = name

class Student(Person):
	def __init__(self,name):
		# super(Student,self).__init__(name)
		print("this is child class")
		Person.__init__(self,name)   #旧式类的调用父类

s1 = Student('xxx')
print(s1.name)
```