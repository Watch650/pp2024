class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id, "No mark for this course")
    
    def input_mark(self):
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark for course: "))
        self.add_mark(course_id, mark)
        
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
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.add_student(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.add_course(course)


school = School()

school.input_students()
school.input_courses()

for student_id in school.students:
    print(f"Entering marks for student ID: {student_id}")
    school.students[student_id].input_mark()

school.list_students()
school.list_courses()

course_id = input("Enter course ID to show student marks: ")
for student_id in school.students:
    school.show_student_marks(student_id, course_id)