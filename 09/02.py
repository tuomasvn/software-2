from car import Car

car = Car("ABC-123", "142")

print(f"""registration number: {car.reg_num}
max speed: {car.max_speed}kmh
current speed: {car.current_speed}kmh
travelled distance: {car.distance}km
------------------""")

car.accelerate(30)

print(f"current speed: {car.current_speed}")

car.accelerate(70)

print(f"current speed: {car.current_speed}")

car.accelerate(50)

print(f"current speed: {car.current_speed}")

car.accelerate(-200)

print(f"current speed: {car.current_speed}")