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