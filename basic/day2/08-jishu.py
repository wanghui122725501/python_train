index = 1 
while index <= 10:
	if index %2 == 0:
		index += 1
		continue
	print("奇数是：%d"%index)
	index += 1
