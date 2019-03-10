try:
	a = 1
	b = 0
	c = a/b
	print('%.2f'%c)
	print(e)
# except (Exception,NameError):
# 	print("抛出异常")
except ZeroDivisionError as error:
	print("除零异常")
	print(error.args)
else:
	print("没有异常。。。")
finally:
	print("不管有没有异常，都执行")
print("xxx")