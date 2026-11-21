
import random

# Generate rainfall readings for 365 days
readings = [random.randint(0, 20) for _ in range(365)]

# Weekly rainfall totals using slicing
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, len(readings), 7)
]

# Maximum and minimum rainfall
print("Wettest day:", max(readings), "Day:", readings.index(max(readings)) + 1)
print("Driest day:", min(readings), "Day:", readings.index(min(readings)) + 1)

# 7-day moving average
moving_average = [
    sum(readings[i:i+7]) / 7
    for i in range(len(readings) - 6)
]

# Dry days
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("Weekly totals:", weekly_totals)
print("7-day moving averages:", moving_average)
print("Dry days:", dry_days)
