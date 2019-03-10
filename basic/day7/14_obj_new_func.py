class Car(object):
	def __new__(cls,*args,**kwargs):
		print('new method')
		return super(Car,cls).__new__(cls,*args,**kwargs)

	def __init__(self):
		print('car in method')

c = Car()
print(c)