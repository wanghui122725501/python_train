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

## 多继承

注意事项：
```
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
```

## 多态
```
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
```

### 实例属性
- 绑定到对象上的属性就叫做实例属性
- 实例属性只在当前的对象上有用
```
class Person(object):
	def __init__(self,name):
		self.name = name

p1 = Person('xx')
p1.age = 12
print(p1.name)

p2 = Person('xxoo')
# print(p2.age) #报错
print(p2.name)
```
### 类属性
在类中定义类属性,
如果通过对象修改类属性，那么其实不是修改类属性，而是在这个对象上重新定义了一个名字一样的实例属性
```
class Person(object):
	country = 'china' 
	def __init__(self,name):
		self.name = name

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
```

### 实例方法和类方法
```
class Person(object):
	def eat(self):
		print('hello')

	@classmethod
	def greet(cls):
		print("ccc")

p1 = Person()
#实例方法
p1.eat()
# Person.eat()#不能执行

#类方法
Person.greet()
```

### 静态方法
不需要修改类或者对象的时候，并且这个方法放在类中显得代码有管理型
staticmethod
```
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
		print('xxooxxooxxx')
p1.st_md()
Person.st_md()
```

## new方法
创建对象使用的就是`__new__`方法，调用对象使用`__init__`
```
class Car(object):
	def __new__(cls,*args,**kwargs):
		print('new method')
		return super(Car,cls).__new__(cls,*args,**kwargs)

	def __init__(self):
		print('car in method')

c = Car()
print(c)
```