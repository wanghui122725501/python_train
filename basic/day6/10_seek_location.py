f = open('notex.md','r',encoding='utf-8')
'''
current_location = f.tell()
print(current_location)
f.seek(5,0) # 从文件起始位置光标向后移动五位
text = f.read()
print(text)
'''

# 获取文件末尾三位的值
f.seek(0,2)   #将光标定位到文件末尾
current_end = f.tell()
tmp = current_end - 3  #保留的位数
f.seek(tmp,0)
text = f.read()
print(text)
f.close()