

class CPU(object):
	"""
	cpu
	"""
	def __init__(self,brand,core,interface):
		self.brand = brand
		self.core = core
		self.interface = interface

def RAM(object):
	"""
	RAM
	"""
	def __init__(self,brand,size):
		self.brand = brand
		self.size = size

def Disk(object):
	"""
	DISK
	"""
	def __init__(self,brand,size):
		self.brand = brand
		self.size = size


def Computer(object):
	"""
	Computer class
	"""
	def __init__(self,cpu_interface,ram_count,disk_count):
		self.cpu_interface = cpu_interface
		self.ram_count = ram_count
		self.disk_count = disk_count
		self.__cpu = None
		self.__rams = []
		self.__disks = []

	def add_cpu(self,cpu):
		if cpu.interface == self.cpu_interface:
			self.__cpu = cpu
		else:
			print("CPU ERROR!不能安装！")

	def add_ram(self,ram):
		if len(self.__rams) == self.ram_count:
			print("内存位置满！")
		else:
			self.__rams.append(ram)

	def add_disk(self,disk):
		if len(self.__disks) == self.disk_count:
			print("磁盘位置满")
		else:
			self.__disks.append(disk)

	def run(self):
		if not self.__cpu:
			print("没有cpu，不能运行")
			return
		elif len(self.__rams) == 0 or len(self.__rams) > self.ram_count:
			print("内存没有，电脑不能正常运行！")
			return
		elif len(self.__disks) == 0 or len(self.__disks) > self.disk_count:
			print("没有磁盘，电脑不能运行！")
			return
		else:
			print("配件都安装好了，Running!!")
def main():
	computer = Computer('1212',2,2)
	cpu = CPU('inter',4,'x86_64')
	ram1 = RAM('kingstone','4G')
	ram2 = RAM('kingstone','4G')
	disk1 = Disk('tonshba','512G')
	disk2 = Disk('tonshba','512G')

	computer.add_cpu(cpu)
	computer.add_ram(ram1)
	computer.add_ram(ram2)
	computer.add_disk(disk1)
	computer.add_disk(disk2)

	computer.run()


if __name__ == '__main__':
	main()