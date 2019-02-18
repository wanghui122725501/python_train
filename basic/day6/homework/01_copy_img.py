source_path = input("请输入图片的原地址")
dest_path = input("请输入保存的地址")

with open(source_path,'rb') as f1:
	with open(dest_path,'wb') as f2:
		f2.write(f1.read())

print("保存成功")