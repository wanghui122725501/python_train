row = 1
column = 1
while row <= 9:
	while column <= row:
		print("%d*%d=%d"%(row,column,row*column),end=" ")
		column += 1
	row += 1
	print("\n")
	column = 1