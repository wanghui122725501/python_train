
user = {
	'is_login':True
}

def login_required(func):
	def wrapper(*args,**kwargs):
		if user['is_login'] == True:
			func(*args,**kwargs)
		else:
			print("No Permission!!")
	return wrapper

@login_required
def edit_user(username):
	print("Edit user %s success!"%username)


@login_required
def add_article(title,content):
	print('add %s success content is %s'%(title,content))

edit_user('xxoo')


add_article('titiles A','sdasdjhajsh')