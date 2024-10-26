from car import Car

car = Car("ABC-123", "142")

print(f"""registration number: {car.reg_num}
max speed: {car.max_speed}kmh
current speed: {car.current_speed}kmh
travelled distance: {car.distance}km
------------------""")

car.accelerate(100)

print(f"Current speed: {car.current_speed}")

car.drive(1)

print(f"Distance driven: {car.distance}")