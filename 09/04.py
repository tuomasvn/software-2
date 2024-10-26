import random
from car import Car

cars = []
live = True
line = "---------------"

for new_car in range(10):
	new_car = Car(f"ABC-{new_car + 1}", random.randint(100, 200))
	cars.append(new_car)

for car_check in cars:
	print(f"{car_check.max_speed}, {car_check.reg_num}")

while live:
	for car_for_distance_check in cars:
		distance = car_for_distance_check.distance
		print(f"{car_for_distance_check.reg_num}: {distance}")
		if distance > 10000:
			live = False
			first_to_10k = car_for_distance_check
			break
	if live:
		print("---next hour---")
		for car_accelerate in cars:
			car_accelerate.accelerate(random.randint(-10, 15))

		for car_drive in cars:
			car_drive.drive(1)

for car_final in cars:
	print(line)
	print(f"{car_final.reg_num}")
	print(f"{car_final.current_speed}")
	print(f"{car_final.max_speed}")
	print(f"{car_final.distance}")
print(line)
print(f"{first_to_10k.reg_num} is the winner!")
