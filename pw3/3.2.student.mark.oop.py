import math
import curses

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
        # Calculate the total credits
            total_credits = sum(mark['credit'] for mark in self.marks.values())
        
        # Calculate the weighted sum of marks
            weighted_sum = sum([mark['mark'] * mark['credit'] for mark in self.marks.values()])
        
        # Calculate the GPA as the weighted sum divided by the total credits
            gpa = weighted_sum / total_credits
            return gpa
        else:
            return "No marks found"

def main(stdscr):
    # Initialize curses
    # curses.curs_set(0)
    stdscr.clear()
    
    # Define a dictionary to store students and courses
    students = {}
    courses = {}
    
    # Main loop
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "School Management System")
        stdscr.addstr(2, 0, "1. Add Student")
        stdscr.addstr(3, 0, "2. Add Course")
        stdscr.addstr(4, 0, "3. Input Marks for Student")
        stdscr.addstr(5, 0, "4. Show Student Marks")
        stdscr.addstr(6, 0, "5. List Students")
        stdscr.addstr(7, 0, "6. List Courses")
        stdscr.addstr(8, 0, "7. Exit")
        stdscr.refresh()
        
        # Get user input
        choice = stdscr.getch()
        
        if choice == ord('1'):
            # Add Student
            stdscr.clear()
            stdscr.addstr(0, 0, "Add Student")
            stdscr.addstr(2, 0, "Enter ID: ")
            stdscr.refresh()
            id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, "Enter Name: ")
            stdscr.refresh()
            name = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, "Enter date of birth: ")
            stdscr.refresh()
            dob = stdscr.getstr().decode('utf-8')
            students[id] = Student(id, name, dob)
            stdscr.addstr(5, 0, "Student added successfully.")
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('2'):
            # Add Course
            stdscr.clear()
            stdscr.addstr(0, 0, "Add Course")
            stdscr.addstr(2, 0, "Enter ID: ")
            stdscr.refresh()
            id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, "Enter Name: ")
            stdscr.refresh()
            name = stdscr.getstr().decode('utf-8')
            courses[id] = name
            stdscr.addstr(5, 0, "Course added successfully.")
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('3'):
            # Input Marks for Student
            stdscr.clear()
            stdscr.addstr(0, 0, "Input Marks for Student")
            stdscr.addstr(2, 0, "Enter Student ID: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, "Enter Course ID: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(3, 0, "Enter Mark: ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode('utf-8'))
            mark = math.floor(mark * 10) / 10
            stdscr.addstr(3, 0, "Enter Credit: ")
            stdscr.refresh()
            credit = float(stdscr.getstr().decode('utf-8'))
            if student_id in students:
                students[student_id].add_mark(course_id, mark, credit)
                stdscr.addstr(6, 0, "Mark added successfully.")
            else:
                stdscr.addstr(6, 0, "Student not found.")
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('4'):
            # Show Student mark
            stdscr.clear()
            stdscr.addstr(0, 0, "Show Student marks")
            stdscr.addstr(2, 0, "Enter Student ID: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(2, 0, "Enter Course ID: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode('utf-8')

            if student_id in students:
                student = students[student_id]
                if course_id in student.marks[course_id]['mark']:
                    mark = student.marks[course_id]['mark']
                    stdscr.addstr(4, 0, f"Mark for course {course_id}: {mark}")
                else:
                    stdscr.addstr(4, 0, f"Mark not found.")
            else:
                stdscr.addstr(4, 0, "Student not found.")
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('5'):
            # List Students
            stdscr.clear()
            stdscr.addstr(0, 0, "Students")
            # Sort students by GPA in descending order
            sorted_students = sorted(students.items(), key=lambda item: item[1].calculateGPA(), reverse=True)
            for i, (id, student) in enumerate(sorted_students, start=2):
                stdscr.addstr(i, 0, f"{id}: {student.name} - GPA: {student.calculateGPA()}")
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('6'):
            # List Courses
            stdscr.clear()
            stdscr.addstr(0, 0, "Courses")
            for i, (id, name) in enumerate(courses.items(), start=2):
                stdscr.addstr(i, 0, f"{id}: {name}")
            stdscr.refresh()
            stdscr.getch()
        
        elif choice == ord('7'):
            # Exit
            break

# Run the application
curses.wrapper(main)
