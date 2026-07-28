import json

def get_students():
    try:
        with open("students.json") as file:
            student = json.load(file)
            return student
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent = 4)

def add_student():
    students = get_students()

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))

    student = {
        "Name" : name,
        "Age" : age,
        "Marks" : marks
    }

    students.append(student)
    save_students(students)
    print("\nStudent Added Successfully!.")


def display_students():
    students = get_students()

    if not students:
        print("\nNo students to display.")

    print("*" * 30)
    print("Displaying Students: ")
    for student in students:
        print("\nName:", student["Name"])
        print("Age:", student["Age"])
        print("Marks:", student["Marks"])


while True:
    print("\nStudent Management System. ")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        print("Exiting Successfully!.")
        break
    else:
        print("Please enter a valid choice!")




