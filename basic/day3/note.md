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
## 字符串下标操作
```
name = "www.cropy.cn"

#@循环打印
# for i in name:
# 	print(i)

## 下标
a = name[0]
print(a)
b = name[1]
print(b)
```
## 字符串的切片
- 正常切片
- 带步长的切片
```
numbers = "0123456789"
print(numbers[0::2]) #打印偶数
print(numbers[1::2])
print(numbers[::-1])  #逆序打印
```
## 字符串的方法
```
text = "hello cropy"

# find方法
'''
position = text.find("cropy")
if position > 0:
	print("cropy在text中")
else:
	print("cropy不在text中")
'''

# index方法
position = text.index("cropy")
print(position)

# len方法：获取字符串长度
length = len(text)
print(length)

# count出现的次数计算
text1 = "hello python python"
counts = text1.count("python")
print(counts)

# replace：替换,不会改变原来的值
text2 = "hello python python" 
new_test = text2.replace("python","cropy",1)   #1是个数
print(new_test)
print(text2)

# split方法：返回列表
text3 = "hello python cropy"
words = text3.split(" ")  #按照分隔符分割成列表
print(words)

# startswith
text4 = "hello python"
if text4.startswith("hello"):
	print("以hello开头！")
else:
	print("不是以hello开头")

# endswith
if text4.endswith("n"):
	print("以n结尾")
else:
	print("不是以n结尾")

# lower
text5 = "As My LOVE!"
text_new1 = text5.lower()
print(text_new1)

# upper
text_6 = text_new1.upper()
print(text_6)

# strip:删除两边的空格。lstrip删除左边的空格，rstrip删除右边的空格
text_7 = "    darshboard    "
new_text2 = text_7.strip() 
new_text3 = text_7.lstrip() 
new_text4 = text_7.rstrip() 
print(new_text2)
print(new_text3)
print(new_text4)

# partition
text_8 = "hello python cropy"
print(text_8.partition("python"))

# isalnum:字母或者数字
text_8 = "hello cropy"
result = text_8.isalnum()
print(result)    #返回false，因为不包含空格

# isalpha
res = text_8.isalpha()
print(res)

# isdigit
# isspace
# format
```
## 转义字符
\ :续行符
\n：换行符
```
text = "hello\
world!"
print(text)

text2 = "hello \nabc"
print(text2)

text3 = "hello aa\'s friends "
print(text3)

text4 = "hello\tdada"
print(text4)

text5 = "\\"
print(text5)
```
## 原生字符串
```
##不做转义
text6 = r'\\\\\t\n'
print(text6)
```
##编码解码
- encode：将unicode转换成bytes
```
texts = "hello word"
# 网路传输或者加密，需要转成bytes
text_bytes = texts.encode('utf-8')
```
- decode
```
# 文件保存到本地
# 将bytes转换成utf-8
text_byte = b'hello world!!'
text1 = text_byte.decode('utf-8')
print(text1)
print(type(text1))
```
## 作业
### 
text = """
 i am xiao xiao,i have over 8 years of experience in marketing,i am the team manager of marketing for HP since 2013
"""
1. 删除以上字符串所有的空格，保存到新的字符串中
2. 盘点以上单词个数
3. 把以上包含了t的单词找出来
4. 把以上的数字找出来
### 使用format链接字符串
DB_USER = 'root'
DB_PASSWORD = 'root'
....  
拼接成mysql+pymysql://username:password@host:port/dbName