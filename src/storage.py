# src/storage.py

import csv
import os
from student import Student

DATA_FILE = os.path.join("data", "students.csv")
DELETED_FILE = os.path.join("data", "students_deleted.csv")
IMPORT_ERRORS_FILE = os.path.join("data", "import_errors.csv")


def row_to_student(row):
    """Convert a CSV row dict into a Student object with correct field mapping"""
    try:
        return Student(
            Roll_No=row["Roll_No"],
            Name=row["Name"],
            Branch=row["Branch"],
            Year=row["Year"],
            Gender=row["Gender"],
            Age=row["Age"],
            Attendance=row["Attendance_%"],
            Mid1=row["Mid1_Marks"],
            Mid2=row["Mid2_Marks"],
            Quiz=row["Quiz_Marks"],
            Final=row["Final_Marks"]
        )
    except Exception as e:
        print(f"⚠ Error creating Student from row {row}: {e}")
        return None


def load_students():
    """Load all students from CSV into Student objects"""
    students = []
    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = row_to_student(row)
            if student:
                students.append(student)
    return students


def save_students(students):
    """Save all Student objects back to CSV"""
    with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Roll_No", "Name", "Branch", "Year", "Gender", "Age",
                "Attendance_%", "Mid1_Marks", "Mid2_Marks",
                "Quiz_Marks", "Final_Marks"
            ]
        )
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())


def add_student(student):
    """Add a new student to the CSV"""
    students = load_students()
    # Check duplicate roll_no
    if any(s.roll_no == student.roll_no for s in students):
        raise ValueError(f"Student with Roll_No {student.roll_no} already exists")

    students.append(student)
    save_students(students)


def update_student(roll_no, updated_data):
    """Update student record by roll_no"""
    students = load_students()
    for s in students:
        if s.roll_no == roll_no:
            # Update allowed fields
            for key, value in updated_data.items():
                if hasattr(s, key):
                    setattr(s, key, value)
            save_students(students)
            return True
    return False


def delete_student(students, roll_no):
    """Delete a student by roll_no and save to deleted file"""
    for s in students:
        if s.roll_no == roll_no:
            students.remove(s)
            # Save to deleted CSV
            with open(DELETED_FILE, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "Roll_No", "Name", "Branch", "Year", "Gender", "Age",
                        "Attendance_%", "Mid1_Marks", "Mid2_Marks",
                        "Quiz_Marks", "Final_Marks"
                    ]
                )
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(s.to_dict())
            save_students(students)
            return True
    return False


def bulk_import(import_file):
    """Import multiple students from another CSV, log errors if any"""
    students = load_students()
    errors = []

    with open(import_file, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                student = row_to_student(row)
                if student:
                    # check duplicate
                    if any(s.roll_no == student.roll_no for s in students):
                        raise ValueError(f"Duplicate Roll_No {student.roll_no}")
                    students.append(student)
                else:
                    errors.append(row)
            except Exception:
                errors.append(row)

    save_students(students)

    # Write errors
    if errors:
        with open(IMPORT_ERRORS_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(errors)
