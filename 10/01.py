from elevator import Elevator

elevator_1 = Elevator(0, 10)

print(f"Current floor:{elevator_1.current_floor}")

elevator_1.go_to_floor(5)

print(f"Current floor:{elevator_1.current_floor}")

elevator_1.go_to_floor(0)

print(f"Current floor:{elevator_1.current_floor}")
