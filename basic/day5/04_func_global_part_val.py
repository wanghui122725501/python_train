
username = "bbb"
def greet():
	username = "aaa"
	print("herllo %s"%username)

print(username)
# greet()

def greet_a():
	# gvlobal关键字，修改全局变量
	global username
	username = "cccc"
	print("hello ",username)
greet_a()
print(username)

persons = ["aaa","bbb"]
def add_persons(name):
	print(persons)
	persons.append(name)

add_persons("ccc")
print(persons)


def persons_global(name):
	global persons
	persons = []
	print(persons)

persons_global("ddd")
print(persons)
