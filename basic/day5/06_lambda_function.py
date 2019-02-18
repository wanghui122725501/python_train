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


def my_cmp(x):
	return x['age']

persons.sort(key=my_cmp)
print(persons)