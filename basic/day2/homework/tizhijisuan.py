gendar = input("请输入性别（男|女）：")
yaowei = int(input("请输入腰围（cm）:"))
height = int(input("请输入体重（kg）："))

while True:
	if gendar == "男":
		a = float(yaowei) * 0.74
		b = float(height) * 0.082 + 44.74
		c = a - b
		tizhi_ratio = (c / float(height)) * 100
		break
	elif gendar == "女":
		a = float(yaowei) * 0.74
		b = float(height) * 0.082 + 34.89
		c = a - b
		tizhi_ratio = (c / float(height)) * 100
		break
print(tizhi_ratio)