import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

import csv

with open("new_students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "course"])
    writer.writerow(["John", 24, "Python"])
    writer.writerow(["Sarah", 23, "Web Development"])

print("Student records saved successfully!")

import csv

with open("new_students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["David", 26, "Data Science"])

print("New student added successfully!")

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(student["name"])
        print(student["course"])

with open("dict_students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "course"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "name": "Kevin",
        "age": 28,
        "course": "Python"
    })

    writer.writerow({
        "name": "Grace",
        "age": 24,
        "course": "Data Science"
    })

print("Dictionary records saved successfully!")
