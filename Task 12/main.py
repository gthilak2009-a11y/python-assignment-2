
readings = [1, 3, 5, 7, 10, 55, -60, 4, 8, 12]

# Clean valid readings
valid = [c for c in readings if -50 <= c <= 50]

# Convert Celsius to Fahrenheit
fahrenheit = [(c * 9/5) + 32 for c in valid]

# Find alarm minutes (temperature outside 2–8 °C)
alarms = [
    (minute, temp)
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
]

# Using map() and filter()
valid_filter = list(filter(lambda c: -50 <= c <= 50, readings))
fahrenheit_map = list(map(lambda c: (c * 9/5) + 32, valid_filter))

# Dictionary comprehension
temperature_dict = {
    minute: temp
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50
}

# Set comprehension
temperature_set = {temp for temp in valid}

print("Valid Celsius:", valid)
print("Fahrenheit:", fahrenheit)
print("Alarm minutes:", alarms)
print("Using filter:", valid_filter)
print("Using map:", fahrenheit_map)
print("Dictionary:", temperature_dict)
print("Set:", temperature_set)
