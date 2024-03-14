# Create dictionaries to store students and courses info
students = []
courses = {}

# Input number of students in a class & info: id, name, DoB
def input_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: \n")
        students.append((id, name, dob, {}))

# Input number of courses & info: id, name
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        id = int(input("Enter course ID: "))
        name = input("Enter course name: \n")
        courses[id] = name

# Input marks for student in this course
def input_marks():
    student_id = int(input("Enter student ID: "))
    course_id = (input("Enter course ID: "))
    mark = float(input("Enter mark for course: \n"))
    for student in students:
        if student[0] == student_id:
            student[3][course_id] = mark

# List courses
def list_courses():
    for course_id, course_name in courses.items():
        print(f"\nCourse ID: {course_id}, Course Name: {course_name}\n")

# List students
def list_students():
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}\n")

# Show student marks for a given course
def show_student_marks(course_id):
    for student in students:
        if course_id in student[3]:
            print(f"Student ID: {student[0]}, Mark: {student[3][course_id]}")

def main():
    input_students()
    input_courses()
    input_marks()
    list_courses()
    list_students()
    show_student_marks(input("Enter course ID to show student marks: "))

main()