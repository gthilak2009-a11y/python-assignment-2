
trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Vijayawada", "12:00", "12:10"),
            ("Hyderabad", "18:00", "18:15")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12602": {
        "name": "Mumbai Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Vijayawada", "13:00", "13:10"),
            ("Mumbai", "22:00", "22:15")
        ],
        "days": {"Tuesday", "Thursday"}
    },

    "12603": {
        "name": "Bangalore Express",
        "stops": [
            ("Bangalore", "08:00", "08:15"),
            ("Chennai", "12:00", "12:10"),
            ("Vijayawada", "18:00", "18:15")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "12604": {
        "name": "Delhi Express",
        "stops": [
            ("Chennai", "09:00", "09:15"),
            ("Vijayawada", "15:00", "15:10"),
            ("Delhi", "23:00", "23:15")
        ],
        "days": {"Wednesday", "Saturday"}
    },

    "12605": {
        "name": "Kolkata Express",
        "stops": [
            ("Chennai", "10:00", "10:15"),
            ("Vijayawada", "16:00", "16:10"),
            ("Kolkata", "23:30", "23:45")
        ],
        "days": {"Monday", "Thursday", "Sunday"}
    }
}

station = input("Enter station: ")
day = input("Enter day: ")

results = []

for number, details in trains.items():
    if day in details["days"]:
        for stop in details["stops"]:
            if stop[0].lower() == station.lower():
                results.append((stop[2], number, details["name"]))
                break

# Sort by departure time
results = sorted(results, key=lambda x: x[0])

if results:
    print("\nTrains available:")
    for departure, number, name in results:
        print(number, name, "Departure:", departure)
else:
    print("No trains found.")

# Print complete timetable
print("\nComplete Timetable:")
for number, details in trains.items():
    print("\nTrain:", number, details["name"])
    print("Running days:", details["days"])

    for stop in details["stops"]:
        print(stop)
