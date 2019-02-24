#coding: utf-8
PETS = []
FILENAME = 'pets.txt'

try:
	with open(FILENAME,'r',encoding="utf-8") as fp:
		for line in fp:
			info = line.split('/')
			ID = info[0]
			name = info[1]
			category = info[2]
			price = info[3]
			PETS.append({'id':ID,'name':name,'category':category,'price':price})


except FileNotFoundError:
	# print("文件不存在！")
	fp = open(FILENAME,'w',encoding='utf-8')
	fp.close()

def add_pet():
	ID = input("请输入编号：").strip()
	name = input("请输入宠物名称：").strip()
	category = input("请输入宠物种类：").strip()
	price = input("请输入宠物价格").strip()
	pet = {"id":ID,"name":name,"category":category,"price":price}
	PETS.append(pet)
	print("宠物添加成功")

def search_pet():
	name = input("请输入宠物名称：").strip()
	for pet in PETS:
		if pet['name'] == name:
			text = "编号：{}，名称：{}，种类{}，价格：{}".format(
					pet["id"],
					pet["name"],
					pet["category"],
					pet["price"],
				)
			print(pet)

def delete_pet():
	ID = input("请输入编号：").strip()
	for pet in PETS:
		if pet['id'] == ID:
			PETS.remove(pet)
			print("恭喜，删除成功")
			break

def list_pet():
	for pet in PETS:
		text = "编号：{}，名称：{}，种类{}，价格：{}".format(
				pet['id'],
				pet['name'],
				pet['category'],
				pet['price'],
			)
		print(text)

def exit_program():
	with open(FILENAME,'w',encoding='utf-8') as fp:
		lines = []
		for pet in PETS:
			text = "{ID}/{name}/{category}/{price}".format(
					ID = pet['id'],
					name = pet['name'],
					category = pet['category'],
					price = pet['price']
			)
			lines.append(text+'\n')
		fp.writelines(lines)

def main():
	print("="*30)
	print("1. 添加宠物")
	print("2. 查找宠物")
	print("3. 删除宠物")
	print("4. 列出宠物")
	print("5. 退出程序")
	print("="*30)
	while True:
		option = input("请输入选项").strip()
		if option == "1":
			add_pet()
		elif option == "2":
			search_pet()
		elif option == "3":
			delete_pet()
		elif option == "4":
			list_pet()
		elif option == "5":
			exit_program()
			break
		else:
			print("请输入正确的选项")

main()