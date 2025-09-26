# src/student.py
from dataclasses import dataclass

@dataclass
class Student:
    roll_no: int
    name: str
    branch: str
    year: int
    gender: str
    age: int
    attendance: float
    mid1: float
    mid2: float
    quiz: float
    final: float

    def validate(self):
        if not isinstance(self.roll_no, int):
            raise ValueError("Roll_No must be integer")
        if not (0 <= self.attendance <= 100):
            raise ValueError("Attendance must be between 0 and 100")
        for mark in [self.mid1, self.mid2, self.quiz, self.final]:
            if not (0 <= mark <= 100):
                raise ValueError("Marks must be between 0 and 100")