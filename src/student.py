# src/student.py

class Student:
    def __init__(self, Roll_No, Name, Branch, Year, Gender, Age, Attendance, Mid1, Mid2, Quiz, Final):
        # Convert and store values
        self.roll_no = int(Roll_No)  # primary key
        self.name = Name.strip()
        self.branch = Branch.strip().upper()
        self.year = int(Year)
        self.gender = Gender.strip().upper()
        self.age = int(Age)
        self.attendance = float(Attendance)
        self.mid1 = float(Mid1)
        self.mid2 = float(Mid2)
        self.quiz = float(Quiz)
        self.final = float(Final)

        # Validation rules
        if not (0 <= self.attendance <= 100):
            raise ValueError("Attendance must be between 0 and 100")
        if not (0 <= self.mid1 <= 20 and 0 <= self.mid2 <= 20 and 0 <= self.quiz <= 10 and 0 <= self.final <= 100):
            raise ValueError("Marks out of allowed range")

    def to_dict(self):
        """Convert to dictionary for CSV writing (with same headers as file)"""
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
