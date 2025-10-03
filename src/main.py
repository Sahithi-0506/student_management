# src/main.py

import pandas as pd
from storage import (
    add_student,
    delete_student,
    update_student,
    bulk_import,
    load_students,
    save_students,
)
from student import Student


def main():
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
            try:
                roll_no = int(input("Roll No: "))
                name = input("Name: ")
                branch = input("Branch: ")
                year = int(input("Year: "))
                gender = input("Gender (M/F): ")
                age = int(input("Age: "))
                attendance = float(input("Attendance %: "))
                mid1 = float(input("Mid1 Marks: "))
                mid2 = float(input("Mid2 Marks: "))
                quiz = float(input("Quiz Marks: "))
                final = float(input("Final Marks: "))

                student = Student(
                    Roll_No=roll_no,
                    Name=name,
                    Branch=branch,
                    Year=year,
                    Gender=gender,
                    Age=age,
                    Attendance=attendance,
                    Mid1=mid1,
                    Mid2=mid2,
                    Quiz=quiz,
                    Final=final,
                )

                add_student(student)
                print("✅ Student added successfully!")

            except Exception as e:
                print(f"⚠ Error: {e}")

        elif choice == "2":
            roll_no = int(input("Enter Roll No to search: "))
            students = load_students()
            found = [s for s in students if s.roll_no == roll_no]
            if found:
                df = pd.DataFrame([s.to_dict() for s in found])
                print(df.to_string(index=False))
            else:
                print("❌ Student not found.")

        elif choice == "3":
            roll_no = int(input("Enter Roll No to update: "))
            field = input("Enter field to update (name, branch, year, age, attendance, mid1, mid2, quiz, final): ")
            value = input("Enter new value: ")

            students = load_students()
            updated = False
            for s in students:
                if s.roll_no == roll_no:
                    # match input field to attribute
                    field_map = {
                        "name": "name",
                        "branch": "branch",
                        "year": "year",
                        "gender": "gender",
                        "age": "age",
                        "attendance": "attendance",
                        "mid1": "mid1",
                        "mid2": "mid2",
                        "quiz": "quiz",
                        "final": "final",
                    }
                    if field.lower() in field_map:
                        attr = field_map[field.lower()]
                        # cast types properly
                        if attr in ["year", "age", "mid1", "mid2", "quiz", "final", "attendance"]:
                            value = float(value)
                        setattr(s, attr, value)
                        save_students(students)
                        updated = True
                        print("✅ Student updated successfully!")
                    break
            if not updated:
                print("❌ Student not found or invalid field.")

        elif choice == "4":
            roll_no = int(input("Enter Roll No to delete: "))
            students = load_students()
            if delete_student(students, roll_no):
                print("✅ Student deleted and moved to deleted file.")
            else:
                print("❌ Student not found.")

        elif choice == "5":
            from reports import generate_reports
            generate_reports()


        elif choice == "6":
            import_file = input("Enter import CSV file path: ")
            bulk_import(import_file)
            print("✅ Bulk import completed. Check import_errors.csv for issues.")

        elif choice == "7":
            students = load_students()
            if not students:
                print("No students found.")
            else:
                df = pd.DataFrame([s.to_dict() for s in students])
                print("\n--- All Students ---")
                print(df.to_string(index=False))

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
