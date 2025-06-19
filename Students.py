# student_core.py

import json
import os

class Student:
    def __init__(self, name, age, roll, email, dept):
        self.name = name
        self.age = age
        self.roll = roll
        self.email = email
        self.dept = dept

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "roll": self.roll,
            "email": self.email,
            "dept": self.dept
        }

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Roll No: {self.roll} | Email: {self.email} | Dept: {self.dept}"

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self, name, age, roll, email, dept):
        self.students.append(Student(name, age, roll, email, dept))
        self.save_to_file()

    def get_all_students(self):
        return self.students

    def find_by_roll(self, roll):
        return [s for s in self.students if s.roll == roll]

    def delete_by_roll(self, roll):
        self.students = [s for s in self.students if s.roll != roll]
        self.save_to_file()

    def sort_by_name(self):
        self.students.sort(key=lambda s: s.name.lower())
        self.save_to_file()

    def sort_by_roll(self):
        self.students.sort(key=lambda s: s.roll)
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.students = [Student(**d) for d in data]
