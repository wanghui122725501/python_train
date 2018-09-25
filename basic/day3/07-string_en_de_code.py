texts = "hello word"
# 网路传输或者加密，需要转成bytes
text_bytes = texts.encode('utf-8')
print(text_bytes)
print(type(text_bytes))

# 将bytes转换成utf-8
text_byte = b'hello world!!'
text1 = text_byte.decode('utf-8')
print(text1)
print(type(text1))

from hashlib import md5
a = 'hello word'
res = md5(a.encode('utf-8')).hexdigest()
print(res)