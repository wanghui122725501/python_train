# numbers = [23,14,100,12]
# numbers.sort(reverse=True)
from functools import cmp_to_key

persons = [
	{
		'name':"changsan",
		'age':12
	},
	{
		'name':"zhangsan1",
		'age':23
	},
	{
		'name':"shangsan2",
		'age':31
	},
	{
		'name':"yangsan3",
		'age':51
	},
	{
		'name':"dangsan4",
		'age':13
	},
]

def cmp(a,b):
	if a['age'] > b['age']:
		return 1
	elif a['age'] < b['age']:
		return -1
	else:
		if a['name'] > b['name']:
			return 1
		else:
			return -1
#sort会改变原列表的数据
#sorted不会改变元列表的数据，返回一个新的数据
persons.sort(key=cmp_to_key(cmp)

new_per = sorted(persons,key=cmp_to_key(cmp))
print(new_per)