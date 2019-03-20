

class Plane(object):
	def __init__(self):
		self._alive = True
		self._score = 0
    
    #将alive方法设置成属性，以后调用后tmp = p.alive,就会执行这个方法
	@property
	def alive(self):
		if not self._alive:
			self.cancel_schedule()
		return self._alive

	#给alive添加set属性
	@alive.setter
	def alive(self,value):
		self._alive = value
		if value == False:
			self.die_action()

	def cancel_schedule(self):
		print("取消时间调度！")

    @property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		self._score = value
		self._update_score_brand(value)

	def _update_score_brand(self,value):
		print("积分榜的值%d"%value)

	def die_action(self):
		print("dead Plane")

p = Plane()

hit = True
if hit:
	# p.set_alive(False)
	# p.get_alive()
	# p.alive = False
	temp = p.alive
	print(temp)
	temp2 = p.score
	print(temp2)
	p.set_score(100)
