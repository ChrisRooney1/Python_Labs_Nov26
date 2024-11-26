fuel_per_lap = 2.25
num_of_laps = 45

fuel_requirement = fuel_per_lap * num_of_laps

starting_fuel = fuel_requirement * 1.5

additional_fuel = starting_fuel - 5

first_lap_time = 80.45 + ((additional_fuel / 10) * 0.35)

print(fuel_requirement)
print(starting_fuel)
print(first_lap_time)
