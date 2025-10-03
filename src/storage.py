# src/storage.py
import csv, os
from student import Student

STUDENTS_FILE = "data/students.csv"
DELETED_FILE = "data/students_deleted.csv"
IMPORT_ERRORS = "data/import_errors.csv"

def load_students():
    students = []
    if not os.path.exists(STUDENTS_FILE):
        return students
    with open(STUDENTS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                students.append(Student(**row))
            except Exception as e:
                print(f"⚠ Skipping invalid row: {row} ({e})")
    return students

def save_students(students):
    with open(STUDENTS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=Student(0,"","",0,"",0,0,0,0,0,0).to_dict().keys())
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())

def add_student(student):
    students = load_students()
    # check duplicate roll no
    if any(s.roll_no == student.roll_no for s in students):
        raise ValueError("Duplicate Roll Number")
    students.append(student)
    save_students(students)

def delete_student(roll_no):
    students = load_students()
    remaining = [s for s in students if s.roll_no != roll_no]
    deleted = [s for s in students if s.roll_no == roll_no]

    if deleted:
        with open(DELETED_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=deleted[0].to_dict().keys())
            if f.tell() == 0:  # write header if file is empty
                writer.writeheader()
            for s in deleted:
                writer.writerow(s.to_dict())

    save_students(remaining)

def update_student(roll_no, field, new_value):
    students = load_students()
    updated = False
    for s in students:
        if s.roll_no == roll_no:
            old_value = getattr(s, field)
            setattr(s, field, new_value)
            updated = True
            print(f"Updated {field}: {old_value} → {new_value}")
    if updated:
        save_students(students)
    else:
        print("Student not found.")

def bulk_import(file_path):
    students = load_students()
    errors = []
    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):  # start=2 (skip header)
            try:
                st = Student(**row)
                if any(s.roll_no == st.roll_no for s in students):
                    raise ValueError("Duplicate Roll Number")
                students.append(st)
            except Exception as e:
                errors.append({"Line_No": idx, "Error": str(e), "Data": row})

    save_students(students)

    if errors:
        with open(IMPORT_ERRORS, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Line_No", "Error", "Data"])
            writer.writeheader()
            writer.writerows(errors)
