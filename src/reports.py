# src/reports.py
import csv, os
from storage import load_students

REPORTS_DIR = "data/reports/"

def grade(final_marks):
    if final_marks >= 85: return "A"
    elif final_marks >= 70: return "B"
    elif final_marks >= 50: return "C"
    else: return "D"

def generate_report(branch, year):
    students = [s for s in load_students() if s.branch == branch and s.year == year]

    if not students:
        print("No students found for this branch/year")
        return

    total = len(students)
    avg = sum(s.final for s in students) / total
    highest = max(s.final for s in students)
    lowest = min(s.final for s in students)

    grade_counts = {"A":0,"B":0,"C":0,"D":0}
    for s in students:
        grade_counts[grade(s.final)] += 1

    # print in console
    print(f"\nReport for {branch} Year {year}")
    print(f"Total Students: {total}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Highest: {highest}, Lowest: {lowest}")
    print("Grades:", grade_counts)

    # save to CSV
    os.makedirs(REPORTS_DIR, exist_ok=True)
    file_path = os.path.join(REPORTS_DIR, f"report_{branch}_{year}.csv")
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Students", total])
        writer.writerow(["Average Marks", round(avg,2)])
        writer.writerow(["Highest Marks", highest])
        writer.writerow(["Lowest Marks", lowest])
        for g, cnt in grade_counts.items():
            writer.writerow([f"Grade {g}", cnt])
