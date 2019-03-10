
def get_request(url):
	print("your url is",url)
	return {'msg':url}

def post_request(url):
	print('you %s is downloaded'%url)
	return {'msg':'success'}