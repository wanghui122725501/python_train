__all__ = ['GLOBAL_ZHILIAO','hello','Person']
GLOBAL_ZHILIAO = "zhiliao"

def hello():
	print("hello")

class Person(object):
	def __init__(self):
		print("person init method")