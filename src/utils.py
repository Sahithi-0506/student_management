# src/utils.py
def input_student():
    try:
        roll_no = int(input("Roll No: "))
        name = input("Name: ")
        branch = input("Branch: ")
        year = int(input("Year: "))
        gender = input("Gender (M/F): ")
        age = int(input("Age: "))
        attendance = float(input("Attendance %: "))
        mid1 = float(input("Mid1 Marks (0-20): "))
        mid2 = float(input("Mid2 Marks (0-20): "))
        quiz = float(input("Quiz Marks (0-10): "))
        final = float(input("Final Marks (0-100): "))
        return roll_no, name, branch, year, gender, age, attendance, mid1, mid2, quiz, final
    except Exception as e:
        print(f"Invalid input: {e}")
        return None
