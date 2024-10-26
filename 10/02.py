from building import Building

def elevator_check(building_of_interest):
	print("----------------------------")
	print(f"Building: {building_of_interest}")
	for thing in building_of_interest.elevators_in_building:
		print("----------------------------")
		print(f"Elevator {thing.id} is on floor {thing.current_floor}")
	print("----------------------------")

new_building = Building(0, 5, 3)

elevator_check(new_building)

new_building.run_elevator(0, 3)

elevator_check(new_building)

while True:
	new_building.run_elevator(int(input("elevator id")), int(input("floor to go to")))
	# ^^ BAD !!!! ^^