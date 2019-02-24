#coding: utf-8
import hashlib
import getpass
from functools import reduce

PASSWORD_FILE_NAME = 'password_book.txt'
PASSWORD = None

def login_check():
	"""
	检查用户输入的密码是否正确
	"""
	def check_password(pwd):
		with open(PASSWORD_FILE_NAME,'r') as fp:
			hashed_pwd = fp.readline().replace('\n','')
			if hashlib.md5(bytes(pwd,encoding='utf-8')).hexdigest() ==  hashed_pwd:
				global PASSWORD
				PASSWORD = pwd
				return True
			else:
				return False

	while True:
		pwd = getpass.getpass("请输入登陆密码：")
		if check_password(pwd):
			return True
		else:
			print("密码错误，请重新输入！")

def init_password():
	"""
	第一次使用这个系统，初始化密码
	"""
	init_pwd = None
