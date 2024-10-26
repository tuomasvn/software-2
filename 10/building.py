from elevator import Elevator
class Building:
	def __init__(self, bottom_floor, top_floor, num_elev):
		self.bottom_floor = bottom_floor
		self.top_floor = top_floor
		self.num_elev = num_elev
		self.elevators_in_building = []
		for new_elevator in range(num_elev):
			created_elevator = Elevator(self.bottom_floor, self.top_floor)
			created_elevator.id = new_elevator
			self.elevators_in_building.append(created_elevator)

	def run_elevator(self, elevator_id, dest_floor):
		self.elevators_in_building[elevator_id].go_to_floor(dest_floor)

	def fire_alarm(self):
		for thing in self.elevators_in_building:
			thing.go_to_floor(self.bottom_floor)
