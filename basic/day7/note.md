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

