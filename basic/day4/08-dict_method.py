person = {"username":"wanghui","age":19,"height":140}
'''
print(person)
person.clear()
print(person)
'''

'''
username = person['username']
username1 = person.get('username1')
print(username)
'''

'''
age = person.pop('age')
print(age)
print(person)
'''

'''
value = person.popitem()
print(value)   #返回元组类型
print(person)
'''

'''
student = {'classname':'science','sid':123,"username":"sss"}    #覆盖
person.update(student)
print(person)
'''

username = person.setdefault('username1',"ssddd")
print(username)