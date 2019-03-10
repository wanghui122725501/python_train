
class User(object):
	__instance = None

	def __new__(cls,*args,**kwargs):
		if not cls.__instance:
			cls.__instance = super(User,cls).__new__(cls,*args,**kwargs)
		return cls.__instance

	def __init__(self,name):
		self.name = name

	def share_user(cls):
		if not cls.__instance:
			return User()
			
user1 = User('aaa')
user2 = User('bbb')

print(id(user1))
print(id(user2))