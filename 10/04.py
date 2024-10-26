from race import Race
from car import Car
import random

cars2 = []
round = 0

for new_car in range(10):
    new_car = Car(f"ABC-{new_car + 1}", random.randint(100, 200))
    cars2.append(new_car)

gdd = Race("Grand Demolition Derby", 8000, cars2)

gdd.print_status()

race_done = gdd.race_finished()


while not race_done:
	print(f"Round: {round}")
	gdd.hour_passes()
	if round % 10 == 0:
		gdd.print_status()
	if gdd.race_finished():
		break
	round += 1

print("DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
gdd.print_status()
