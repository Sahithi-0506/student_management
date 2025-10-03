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
            Attendance=row["Attendance_%"],   # map CSV → Python arg
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
            return True
    return False
