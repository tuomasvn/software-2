from car import Car

class ElectricCar(Car):
	def __init__(self, reg_num, max_speed, kwh):
		super().__init__(reg_num, max_speed)
		self.kwh = kwh

class GasolineCar(Car):
	def __init__(self, reg_num, max_speed, tank):
		super().__init__(reg_num, max_speed)
		self.tank = tank

line = "------------"

mada = ElectricCar("ABC-15", 180, 52.5)
gascar = GasolineCar("ACD-123", 165, 32.3)
print(line)
print("accelerating both cars by 1000kmh")
mada.accelerate(1000)
gascar.accelerate(1000)
print(line)
print(f"electric car speed: {mada.current_speed}kmh")
print(f"gasoline car speed: {gascar.current_speed}kmh")
print(line)
print("driving 3 hours")
mada.drive(3)
gascar.drive(3)
print(line)
print(f"electric car driven distance: {mada.distance}km")
print(f"gasoline car driven distance: {gascar.distance}km")