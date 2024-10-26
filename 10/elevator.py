class Elevator:
	def __init__(self, bottom_floor, top_floor):
		self.bottom_floor = bottom_floor
		self.top_floor = top_floor
		self.current_floor = bottom_floor
		self.id = id

	def go_to_floor(self, new_floor):
		if new_floor not in range(self.bottom_floor, self.top_floor+1):
			print("invalid floor")
			return
		"""
		if new_floor > self.top_floor or new_floor < self.bottom_floor:
			print("invalid floor")
			return
		"""
		if new_floor > self.current_floor:
			for floors in range(new_floor - self.current_floor):
				self.floor_up()

		if new_floor < self.current_floor:
			for floors in range(self.current_floor - new_floor):
				self.floor_down()
	
	def floor_up(self):
		self.current_floor += 1
		print(f"The elevator is now on floor {self.current_floor}")

	def floor_down(self):
		self.current_floor -= 1
		print(f"The elevator is now on floor {self.current_floor}")
