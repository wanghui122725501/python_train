

user = {
	"is_login":True
}

# def edit_user():
# 	if user['is_login'] == True:
# 		print("user edit success")
# 	else:
# 		print("return to login page")

# def add_post():
# 	if user['is_login'] == True:
# 		print("article add success")
# 	else:
# 		print("return to login page")

# edit_user()
# add_post()

def case2():
	def login_required(func):
		if user['is_login'] == True:
			func()
		else:
			print("return to login page!!")


	def edit_user():
		print("edit user success!!")

	def add_post():
		print("add article success!!")

	login_required(edit_user)

def case3():
	def login_required(func):
		def wapper():
			if user['is_login'] == True:
				func()
			else:
				print("redirect login page!!")
		return wapper

	@login_required	
	def edit_user():
		print("edit user success!!")

	def add_post():
		print("add article success!!")

	edit_user()

case3()