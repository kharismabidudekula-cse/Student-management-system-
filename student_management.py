students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "roll_no": roll_no,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        roll_no = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter roll number to delete: ")

        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
