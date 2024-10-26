class Car:
	def __init__(self, reg_num, max_speed, current_speed = 0, distance = 0):
		self.reg_num = reg_num
		self.max_speed = int(max_speed)
		self.current_speed = current_speed
		self.distance = distance

	def accelerate(self, change):
		self.current_speed += change
		if self.current_speed > self.max_speed:
			self.current_speed = self.max_speed
		if self.current_speed < 0:
			self.current_speed = 0

	def drive(self, hours):
		self.distance += hours * self.current_speed