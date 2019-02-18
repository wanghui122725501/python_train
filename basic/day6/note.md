# 文件操作
[toc]
## 打开和关闭文件
```
# 1. 以指定的方式打开文件
f = open('notex.md','w')
# 2. 做相关的操作
f.write('# aaa')
# 3. 关闭文件
f.close()
```
## 打开文件的模式

python2: 打开文件的时候使用的是utf8
python3：打开文件使用的是系统自带的文件编码，通过encoding参数来指定编码类型
- r: 文件读
    - r+: 带写入功能的读

- w: 文件写：会覆盖掉原有的数据
    - w+: 读写方式打开文件，不管是读还是写，就会把原来的文件删掉创建一个新的文件，如果要去读取的话，永远读取的都是空的字符串 

- a: 文件追加

## 文件读取
- read函数
```
f = open('xx.txt','r')
s = f.read()
print(s)
f.close()
```
- readline函数
读取一行数据,不能使用for循环去读取，只能采用while循环
```
f = open('notex.md','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line:
		break
	print(line)
f.close()
```
- readlines函数
读取大文件的时候容易消耗系统资源
```
f = open('notex.md','r',encoding='utf-8')
all_lines = f.readlines()
for line in all_lines:
	print(line)
```
- 遍历文件指针对象
大文件的读取方式
```
f = open('note.md','r',encoding='utf-8')
for line in f:
	print(line)
f.close()
```

## 文件写入
- write函数
- writelines()函数
```
f = open('notex.md','w',encoding='utf-8')
a = ['aaa\n','bbb\n','ccc\n']
f.writelines(a)
f.close()
```

## 文件定位操作
- 获取文件指针位置：tell
- 定位光标位置：seek
```
seek(offset,from)
offset：表示偏移量
from：表示相对位置（0：表示文件开头，1：表示从当前位置，2：表示文件末尾）
```

## with语句操作文件
防止忘记close文件句柄，叫做上下文管理器
```
with open('notex.md','a',encoding='utf-8') as f:
	f.write('xxoo')
print('...')
```

## 拷贝文件
```
# coding: utf-8
'''
文件拷贝
'''
tmp = []


'''
方法一
with open('notex.md','r',encoding='utf-8') as f1:
	for line in f1:
		tmp.append(line)

with open('notex_copy.md','w',encoding='utf-8') as f2:
	f2.writelines(tmp)
'''

with open('notex.md','r',encoding='utf-8') as f1:
	with open('notex2.md','w',encoding='utf-8') as f2:
		for line in f1:
			f2.writelines(line)
```

## 移除文件中的病毒代码
尤其注意中间状态这个变量的定义
```
# coding: utf-8

tmp = []

with open('test.html','r',encoding='utf-8') as f1:
	is_extra = False
	for line in f1:
		if line.startswith('<script type="text/javascript">'):
			is_extra = True
		elif line.startswith('</script>'):
			is_extra = False
		else:
			if not is_extra:
				tmp.append(line)

print(tmp)

with open('test.html','w',encoding='utf-8') as f2:
	f2.writelines(tmp)
```
## 作业
- 实现一个复制图片功能的程序
```
E:\十小时大数据入门\第1章 大数据概述\第1章 大数据概述.mp4

```
- 实现一个密码存储系
- 实现一个寄养管理系统