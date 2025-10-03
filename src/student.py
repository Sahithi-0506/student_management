# src/student.py
class Student:
    def __init__(self, roll_no, name, branch, year, gender, age, attendance, mid1, mid2, quiz, final):
        self.roll_no = int(roll_no)  # primary key
        self.name = name.strip()
        self.branch = branch.strip().upper()
        self.year = int(year)
        self.gender = gender.strip().upper()
        self.age = int(age)
        self.attendance = float(attendance)
        self.mid1 = float(mid1)
        self.mid2 = float(mid2)
        self.quiz = float(quiz)
        self.final = float(final)

        # Validation rules
        if not (0 <= self.attendance <= 100):
            raise ValueError("Attendance must be between 0 and 100")
        if not (0 <= self.mid1 <= 20 and 0 <= self.mid2 <= 20 and 0 <= self.quiz <= 10 and 0 <= self.final <= 100):
            raise ValueError("Marks out of allowed range")

    def to_dict(self):
        """Convert to dictionary for CSV writing"""
        return {
            "Roll_No": self.roll_no,
            "Name": self.name,
            "Branch": self.branch,
            "Year": self.year,
            "Gender": self.gender,
            "Age": self.age,
            "Attendance_%": self.attendance,
            "Mid1_Marks": self.mid1,
            "Mid2_Marks": self.mid2,
            "Quiz_Marks": self.quiz,
            "Final_Marks": self.final
        }
