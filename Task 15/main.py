def process_bill(filename):
    total = 0.0
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid number of fields")

                    register_no, name, amount = parts
                    amount = float(amount)

                    total += amount
                    report.append(f"{name} {amount:.2f}")

                except (ValueError, IndexError) as error:
                    rejected.append((line_number, line.strip(), str(error)))

        print("Mess Bill Report")
        for item in report:
            print(item)

        print("Total:", f"{total:.2f}")
        print("Rejected lines:", rejected)

    except FileNotFoundError:
        print("File not found:", filename)

    except PermissionError:
        print("Permission denied:", filename)


filename = "mess_oct.txt"
process_bill(filename)
