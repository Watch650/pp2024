import math
import numpy as np


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
            print(f"Mark for course {course_id} already exists.")

    def get_mark(self, course_id):
        return self.marks.get(course_id, "Mark not found")
    
    def input_mark(self):
        course_id = input("Enter course ID: ")
        mark = float(input(f"Enter mark for course {course_id}: "))
        mark = math.floor(mark * 10) / 10
        credit = float(input(f"Enter credit for course {course_id}: "))
        self.add_mark(course_id, mark, credit)

    def calculateGPA(self):
        if len(self.marks) > 0:
        # Calculate the total credits
            total_credits = sum(mark['credit'] for mark in self.marks.values())
        
        # Calculate the weighted sum of marks
            weighted_sum = sum([mark['mark'] * mark['credit'] for mark in self.marks.values()])
        
        # Calculate the GPA as the weighted sum divided by the total credits
            gpa = weighted_sum / total_credits
            return gpa
        else:
            return "No marks found"
        
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class School:
    def __init__(self):
        self.students= {}
        self.courses= {}

    def add_student(self, student):
        self.students[student.id] = student

    def add_course(self, course):
        self.courses[course.id] = course

    def list_students(self):
        for student_id, student in self.students.items():
            print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

    def list_courses(self):
        for course_id, course in self.courses.items():
            print(f"Course ID: {course.id}, Course name: {course.name}")
    
    def show_student_marks(self, student_id, course_id):
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student.id}, Mark: {student.get_mark(course_id)}")
        else:
            print("Student not found")

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            id = int(input("\nEnter student ID: "))
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.add_student(student)

    def input_courses(self):
        num_courses = int(input("\nEnter number of courses: "))
        for _ in range(num_courses):
            id = input("\nEnter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.add_course(course)

    def calculate_average_gpa(self):
        gpa_list = [student.calculateGPA() for student in self.students.values()]
        if gpa_list:
            return sum(gpa_list) / len(gpa_list)
        else:
            return "No marks found"
    
    def sort_students_by_gpa(self):
        gpa_list = [(student_id, self.students[student_id].calculateGPA()) for student_id in self.students]
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        return gpa_list


school = School()

school.input_students()
school.input_courses()
for course_id in school.courses:
    for student_id in school.students:
        print(f"\nCourse: {course_id}")
        print(f"Entering marks for student ID: {student_id}")
        school.students[student_id].input_mark()

school.list_students()
school.list_courses()

course_id = input("\nEnter course ID to show student marks: ")
for student_id in school.students:
    school.show_student_marks(student_id, course_id)

sorted_students = school.sort_students_by_gpa()
print("\nStudents sorted by GPA:")
for student_id, gpa in sorted_students:
    print(f"Student ID: {student_id}, GPA: {gpa}")

