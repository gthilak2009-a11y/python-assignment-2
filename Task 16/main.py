
from pathlib import Path

folder = Path("attendance")
attendance = {}
errors = []

# Read all CSV files in the attendance folder
for file_path in folder.glob("*.csv"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid number of fields")

                    register_no, date, status = parts

                    if status not in ("P", "A"):
                        raise ValueError("Invalid attendance status")

                    if register_no not in attendance:
                        attendance[register_no] = [0, 0]

                    if status == "P":
                        attendance[register_no][0] += 1
                    else:
                        attendance[register_no][1] += 1

                except ValueError as error:
                    errors.append(
                        (str(file_path), line_number, str(error))
                    )

    except (FileNotFoundError, PermissionError) as error:
        errors.append((str(file_path), 0, str(error)))

# Create attendance report
with open("attendance_report.txt", "w", encoding="utf-8") as report:
    for register_no, counts in attendance.items():
        present, absent = counts
        total = present + absent
        percentage = (present / total) * 100 if total else 0

        report.write(
            f"{register_no}: {percentage:.2f}%\n"
        )

        if percentage < 75:
            print(register_no, "Below 75%:", f"{percentage:.2f}%")

# Create damaged-line report
with open("error_log.txt", "w", encoding="utf-8") as log:
    for error in errors:
        log.write(f"{error}\n")

print("Attendance processing completed.")
