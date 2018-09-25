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