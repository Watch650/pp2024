import math

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark, credit):
        if course_id not in self.marks:
            self.marks[course_id] = {'mark': mark, 'credit': credit}
        else:
            return 0

    def calculateGPA(self):
        if len(self.marks) > 0:
            total_credits = sum(mark['credit'] for mark in self.marks.values())
            weighted_sum = sum([mark['mark'] * mark['credit'] for mark in self.marks.values()])
            gpa = weighted_sum / total_credits
            return gpa
        else:
            return 0.0
