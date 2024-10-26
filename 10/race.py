import random

class Race:
	def __init__(self, name, distance, car_list):
		self.name = name
		self.distance = distance
		self.car_list = car_list

	def hour_passes(self):
		for car in self.car_list:
			car.accelerate(random.randint(-10, 15))

		for car in self.car_list:
			car.drive(1)

	def print_status(self):
		for car in self.car_list:
			print(f'''
			Registration number: {car.reg_num}
			Max speed: {car.max_speed}
			Current speed: {car.current_speed}
			Distance travelled: {car.distance}
			--------------------------------
			''')

	def race_finished(self):
		for car in self.car_list:
			if car.distance >= self.distance:
				return True
