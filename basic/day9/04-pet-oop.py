

class Pet(object):
	"""
	宠物类
	"""
	def __init__(self,pet_id,pet_name,pet_type,pet_price):
		self.id = pet_id
		self.name = pet_name
		self.type = pet_type
		self.price = pet_price

	@classmethod
	def pet_with_line(cls,line):
		pet_id,pet_name,pet_type,pet_price = line.replace('\n','').split('&')
		pet = Pet(pet_id,pet_name,pet_type,pet_price)
		return pet


	def get_line(self):
		line = "{id}&{name}&{type}&{price}\n".format(
				id=self.id,
				name=self.name,
				type=self.type,
				price=self.price
			)
		return line


class PetManager(object):
	__instance = None
	__filename = 'pet_book.txt'
	def __new__(cls,*args,**kwargs):
		if not cls.__instance:
			cls.__instance = super(PetManager,cls).__new__(cls,*args,**kwargs)
		return cls.__instance

	def add_pet(self,pet_id,pet_name,pet_type,pet_price):
		pet = Pet(pet_id,pet_name,pet_type,pet_price)
		with open(PetManager.__filename,'a') as fp:
			line = pet.get_line()
			fp.write(line)

	def list_all_pets(self):
		all_pets = []
		with open(PetManager.__filename,'r') as fp:
			for line in fp:
				pet=Pet.pet_with_line(line)
				all_pets.append(pet)
		return all_pets

	def search_pet(self,name):
		with open(PetManager.__filename,'r') as fp:
			for line in fp:
				pet = Pet.pet_with_line(line)
				if pet.name == name:
					return pet
			return '{"error":"NO Pet Msg!!"}'

# print(Pet.__doc__)   读出类的注释

class Application(object):
	"""
	程序流程控制
	"""
	__instance = None
	def __new__(cls,*args,**kwargs):
		if not cls.__instance:
			cls.__instance = super(Application,cls).__new__(cls,*args,**kwargs)
		return cls.__instance

	def __input_pet_info(self):
		pet_id = input(u"请输入编号：").strip()
		pet_name = input(u"请输入宠物名称：").strip()
		pet_type = input(u"请输入宠物种类：").strip()
		pet_price = input(u"请输入宠物价格").strip()
		manager.add_pet(pet_id,pet_name,pet_type,pet_price)
		print(u'恭喜，宠物添加成功！！')

	def __print_all_pets(self):
		all_pets = manager.list_all_pets()
		print("id\tname\ttype\tprice")
		for pet in all_pets:
			print('{id}\t{name}\t{type}\t{price}'.format(
				id=pet.id,
				name=pet.name,
				type=pet.type,
				price=pet.price
			))


	def run(self):
		print("="*30)
		print("1. 添加宠物")
		print("2. 查找宠物")
		print("3. 删除宠物")
		print("4. 列出宠物")
		print("5. 退出程序")
		print("="*30)
		while True:
			option = int(input(u"请输入序号："))
			if option == 1:
				self.__input_pet_info()
			elif option == 2:
				pass
			elif option == 3:
				pass
			elif option == 4:
				self.__print_all_pets()
			elif option == 5:
				break
			else:
				print("输入信息有误！！")


manager = PetManager()
app = Application()

def main():
	app.run()

if __name__ == '__main__':
	main()