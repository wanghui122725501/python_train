# 列表
[toc]
## 简介
- 容器，方便存储和管理
- 采用中括号定义
- 下表从0开始
## 列表的遍历
- for
- while
```
fruits = ["苹果","香蕉","梨子","菠萝"]

# for 循环版本
# for fruit in fruits:
# 	print(fruit)

# while循环版本
index = 0
while index < len(fruits):
	print(fruits[index])
	index += 1
```
## 基本使用
- 列表嵌套
- 嵌套列表的遍历
- 相加
- 切片操作
- 列表的方法
# 元组
## 定义
- 只读列表
- 四种定义
## 常用的方法
- 下标操作
- 切尔片操作
- 解组操作

## 元组存在的意义
1. 元组在字典当中当做key来使用
2. 在函数中，有时候需要返回多个值，一般采用元组的形式
3. 在一些不希望用户修改值得场景下使用元组来替代列表

# 字典
- 存储key,value键值对的信息
## 基础
- 定义字典
```
people = {"username":"wanghui","age":19,"height":180,"weight":140}
people1 = dict(username="hahah",age=19)
```
- 基本操作
```
len(d）  #获取键值对的长度
d[key]   #获取key对应的value
d[key]=value #设置key对应的value
del d[key]   #删除key
k in d:      #检查k是否在d中
字典中的键可以是任意的不可变数据类型，比如：浮点，整型，字符串或者元组
```
## 常用的方法
- clear：清空字典
- get：访问字典中的键对应的值，如果找不到的话那就是"None"。不会抛异常
- pop：将字典中的某个键删除,并能返回
- popitem：移除字典中的随机一项
- update:合并字典
- setdefault：设置默认值
## 字典的遍历
```
person = {"username":"wanghui","age":19,"height":140}

# 获取key
keys = person.keys()
for key in keys:
	print(key)

#h获取value
values = person.values()
for value in values:
	print(value)

#获取k,v
for key,value in person.items():
	print("key：%s,value:%s"%(key,value))
```
