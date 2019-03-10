from . import my_file
from .my_file import save_data
from .sub_tools import b

def get_request(url):
	print("your url is",url)
	return {'msg':url}

def post_request(url):
	print('you %s is downloaded'%url)
	return {'msg':'success'}

my_file.save_data('xxxxx')