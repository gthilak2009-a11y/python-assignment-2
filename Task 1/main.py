def subsidy_separate(units, ration_card, senior_citizen):
    if units <= 100:
        print("Full Subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial Subsidy")

    if units > 200 and senior_citizen:
        print("Special Subsidy")

    if units > 200 and not senior_citizen:
        print("No Subsidy")


def subsidy_if_elif(units, ration_card, senior_citizen):
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "Partial Subsidy"
    elif units > 200 and senior_citizen:
        return "Special Subsidy"
    else:
        return "No Subsidy"


households = [
    (100, False, False),
    (101, True, False),
    (150, True, False),
    (200, False, False),
    (201, False, False),
    (250, False, True),
    (80, True, True),
    (180, False, True)
]

for h in households:
    units, ration, senior = h
    print(units, ration, senior, ":", subsidy_if_elif(units, ration, senior))
