class ArgumentError(Exception):
	def __init__(self,*args,**kwargs):
		tmp_args = args + (u'参数错误',)
		super(ArgumentError,self).__init__(*tmp_args,**kwargs)
		# print("参数错误")

def greet(name,age):
	if not isinstance(name,str):
		raise ArgumentError('name must be string type')
	if not isinstance(age,int):
		raise ArgumentError('age must be int type')
	print('my name is %s my age is %d'%(name,age))


try:
	greet(123,34)
except Exception as err:
	print(err.args)


# greet(123,333)