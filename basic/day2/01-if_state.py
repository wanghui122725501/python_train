# if else语句
# a = True
# b = False

# # print(type(a))
# if a:
# 	print("True!!")
# 	print("a条件满足！")
# else:
# 	print("False!!!")
# print("Finished!!")

# if 比较运算
'''
a = 1
b = 2
if a == b:
	print("a和b相等！")
else:
	print("a和b不相等！")

username = input("请输入用户名：")
# if username == 'cropy':
if username != 'cropy':
	print("登陆失败！")
else:
	print("登录成功！")
'''
'''
age = 17
if age > 17:   # 可以换成<
	print("可以进入网吧！")
else:
	print("不可以进入网吧！")
'''
# 多条件判断
## and
'''
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "cropy" and password == "123":
	print("登陆成功！")
else:
    print("用户名或者密码错误！")	
'''
## or
## not
'''
person1 = "中国人"
person2 = "其他国家人"
if not person1 == "中国人":
	print("不可以上战舰！")
else:
	print("可以上战舰！")
'''
value = int(input("请输入值："))
if value == 0:
	print("星期天")
elif value == 1:
	print("星期一")
elif value == 2:
	print("星期二")
elif value == 3:
	print("星期三")
elif value == 4:
	print("星期四")
elif value == 5:
	print("星期五")
elif value == 6:
	print("星期六")
else:
	print("输入的不正确")