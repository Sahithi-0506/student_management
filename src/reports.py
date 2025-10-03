# src/reports.py

import os
import pandas as pd
from storage import load_students

REPORTS_FOLDER = os.path.join("data", "reports")
os.makedirs(REPORTS_FOLDER, exist_ok=True)


def calculate_grade(final_marks):
    """Simple grade calculation"""
    if final_marks >= 85:
        return "A"
    elif final_marks >= 70:
        return "B"
    elif final_marks >= 50:
        return "C"
    else:
        return "D"


def generate_reports():
    students = load_students()
    if not students:
        print("No students available to generate reports.")
        return

    # Convert to DataFrame
    df = pd.DataFrame([s.to_dict() for s in students])

    # Add Grade column
    df["Grade"] = df["Final_Marks"].apply(calculate_grade)

    # Group by Branch and Year
    groups = df.groupby(["Branch", "Year"])

    for (branch, year), group in groups:
        total = len(group)
        avg = group["Final_Marks"].mean()
        highest = group["Final_Marks"].max()
        lowest = group["Final_Marks"].min()

        grade_counts = group["Grade"].value_counts().to_dict()

        # Prepare metrics
        report_data = [
            {"Metric": "Total Students", "Value": total},
            {"Metric": "Average Marks", "Value": round(avg, 2)},
            {"Metric": "Highest Marks", "Value": highest},
            {"Metric": "Lowest Marks", "Value": lowest},
            {"Metric": "Grade A", "Value": grade_counts.get("A", 0)},
            {"Metric": "Grade B", "Value": grade_counts.get("B", 0)},
            {"Metric": "Grade C", "Value": grade_counts.get("C", 0)},
            {"Metric": "Grade D", "Value": grade_counts.get("D", 0)},
        ]

        # Save to CSV
        report_file = os.path.join(REPORTS_FOLDER, f"report_{branch}_{year}.csv")
        pd.DataFrame(report_data).to_csv(report_file, index=False)

        print(f"✅ Report generated: {report_file}")
