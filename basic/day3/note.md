# 字符串
[toc]
## 定义
单引号或者双引号成对出现，中间包含内容
## 字符串拼接
- "+" 号拼接
- 占位符形式
```
a = "hello"
b = " world"
c = a + b
print(c)

username = "cropy"
age = 11
greet = "hello my name is %s,my age is %s" %(username,age)
print(greet)
```
## 字符串格式化
- 使用%的形式
- 使用format形式
```
age = 18
text = "my age is %d" %age
print(text)
price = 19.89
print("apple's price is %.2f" %(price))
# format 格式
py = "python"
fr = "cropy.cn"
print("i love {},i stydy from {}".format(py,fr))
print("i love {course_name},i stydy from {class_name}".format(class_name=fr,course_name=py))
```