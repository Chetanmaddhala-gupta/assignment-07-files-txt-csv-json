import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
students = [
    {"name": "Asha", "score": 88},
    {"name": "Rahul", "score": 76},
    {"name": "Meera", "score": 93},
]

# Plain text: one readable record per line.
with (HERE / "students.txt").open("w", encoding="utf-8") as file:
    for student in students:
        file.write(f"{student['name']}: {student['score']}\n")
with (HERE / "students.txt").open(encoding="utf-8") as file:
    print("TXT records:")
    print(file.read(), end="")

# CSV: rows and named columns.
with (HERE / "students.csv").open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)
with (HERE / "students.csv").open(newline="", encoding="utf-8") as file:
    print("CSV records:", list(csv.DictReader(file)))

# JSON: nested and typed data.
with (HERE / "students.json").open("w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)
with (HERE / "students.json").open(encoding="utf-8") as file:
    print("JSON records:", json.load(file))
