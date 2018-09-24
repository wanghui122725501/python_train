#定义要猜的数字
value = 18
input_value = int(input("请输入数字！"))

while input_value != value:
	if input_value > value:
		print("猜大了！")
	elif input_value < value:
		print("猜小了！")
	einput_value = int(input("请输入数字！"))
print("恭喜！猜对了")