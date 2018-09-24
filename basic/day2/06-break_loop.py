'''
index = 1
while index <= 10:
	print(index)
	if  index == 5:
		break
	index += 1
'''
value = 18
input_value = int(input("请输入数字："))
while True:
	if input_value > value:
		print("猜大了！")
	elif input_value < value:
		print("猜小了！")
	else:
		break
	input_value = int(input("请输入数字："))

print("猜对了！")