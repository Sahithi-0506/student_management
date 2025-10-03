# src/main.py
from student import Student
from storage import add_student, delete_student, update_student, bulk_import, load_students
from reports import generate_report
from utils import input_student

def menu():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student (Admission)")
        print("2. Search Student")
        print("3. Update Records")
        print("4. Delete Student")
        print("5. Generate Report")
        print("6. Bulk Import")
        print("7. Show All Students")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input_student()
            if data:
                try:
                    st = Student(*data)
                    add_student(st)
                    print("Student added successfully.")
                except Exception as e:
                    print("Error:", e)

        elif choice == "2":
            key = input("Search by Roll No or Name: ")
            students = load_students()
            found = [s for s in students if str(s.roll_no) == key or key.lower() in s.name.lower()]
            if found:
                for s in found:
                    print(s.to_dict())
            else:
                print("No match found.")

        elif choice == "3":
            roll = int(input("Enter Roll No to update: "))
            field = input("Field to update (attendance/mid1/mid2/quiz/final): ")
            new_value = float(input("Enter new value: "))
            update_student(roll, field, new_value)

        elif choice == "4":
            roll = int(input("Enter Roll No to delete: "))
            confirm = input("Are you sure? (Y/N): ")
            if confirm.lower() == "y":
                delete_student(roll)
                print("Student deleted.")
            else:
                print("Cancelled.")

        elif choice == "5":
            branch = input("Enter Branch: ").upper()
            year = int(input("Enter Year: "))
            generate_report(branch, year)

        elif choice == "6":
            path = input("Enter CSV file path to import: ")
            bulk_import(path)
            print("Bulk import done. Check import_errors.csv if any errors.")

        elif choice == "7":
            students = load_students()
            for s in students:
                print(s.to_dict())

        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
