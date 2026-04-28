students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks1 = int(input("Enter marks in Subject 1: "))
        marks2 = int(input("Enter marks in Subject 2: "))
        marks3 = int(input("Enter marks in Subject 3: "))
        attendance = int(input("Enter attendance percentage: "))

        total = marks1 + marks2 + marks3
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks1": marks1,
            "marks2": marks2,
            "marks3": marks3,
            "attendance": attendance,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Grade:", student["grade"])
                print("Attendance:", student["attendance"], "%")

    elif choice == 3:
        roll_no = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found")
                print("Name:", student["name"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Grade:", student["grade"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        roll_no = input("Enter roll number to update: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                student["name"] = input("Enter new name: ")
                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        roll_no = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
