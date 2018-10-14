person = ("wanghui",19,180,140)
people = {"username":"wanghui","age":19,"height":180,"weight":140}
people1 = dict(username="hahah",age=19)

print(len(person))    #键值对长度
username1 = people['username']
print(username1)  #获取key对应的value
people['username']='hello'
# del people['weight']
print(people)
if 'username' in people:
	print(True)
else:
	print(False)