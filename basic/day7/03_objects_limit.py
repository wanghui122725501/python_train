class Woman(object):

	def __init__(self,age):
		self._age = age


# w = Woman(13)
# print(w._age)


class Account(object):
	def __init__(self,id,passwd):
		self.id = id
		self.__passwd = passwd

	def __account_list(self):
		print("我是私有方法")
		return [11,22,33]

	def get_account_list(self,passwd):
		if passwd == self.__passwd:
			return self.__account_list()

		else:
			return None

a1 = Account('aaa','123456')
a1.get_account_list('123456')
print(a1._Account__passwd)