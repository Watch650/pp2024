import math
import curses
from input import get_input, get_float_input
from output import clear_screen, display_menu, display_message
from domains.student import Student

def main(stdscr):
    # Initialize curses
    clear_screen(stdscr)
    
    # Define a dictionary to store students and courses
    students = {}
    courses = {}
    
    # Main loop
    while True:
        display_menu(stdscr, ["School Management System", "1. Add Student", "2. Add Course", "3. Input Marks for Student", "4. Show Student GPA", "5. List Students", "6. List Courses", "7. Exit"])
        
        # Get user input
        choice = stdscr.getch()
        
        if choice == ord('1'):
            # Add Student
            clear_screen(stdscr)
            display_message(stdscr, 0, "Add Student")
            id = get_input(stdscr, 2, "Enter ID: ", "students.txt")
            name = get_input(stdscr, 2, "Enter Name: ", "students.txt")
            dob = get_input(stdscr, 2, "Enter date of birth: ", "students.txt")
            students[id] = Student(id, name, dob)
            display_message(stdscr, 5, "Student added successfully.")
            stdscr.getch()
        
        elif choice == ord('2'):
            # Add Course
            clear_screen(stdscr)
            display_message(stdscr, 0, "Add Course")
            id = get_input(stdscr, 2, "Enter ID: ", "courses.txt")
            name = get_input(stdscr, 2, "Enter Name: ", "courses.txt")
            courses[id] = name
            display_message(stdscr, 5, "Course added successfully.")
            stdscr.getch()
        
        elif choice == ord('3'):
            # Input Marks for Student
            clear_screen(stdscr)
            display_message(stdscr, 0, "Input Marks for Student")
            student_id = get_input(stdscr, 2, "Enter Student ID: ", "marks.txt")
            course_id = get_input(stdscr, 2, "Enter Course ID: ", "marks.txt")
            mark = get_float_input(stdscr, 3, "Enter Mark: ", "marks.txt")
            mark = math.floor(mark * 10) / 10
            credit = get_float_input(stdscr, 3, "Enter Credit: ", "marks.txt")
            if student_id in students:
                students[student_id].add_mark(course_id, mark, credit)
                display_message(stdscr, 5, "Mark added successfully.")
            else:
                display_message(stdscr, 5, "Student not found.")
            stdscr.getch()
        
        elif choice == ord('4'):
            # Show Student GPA
            clear_screen(stdscr)
            display_message(stdscr, 0, "Show Student GPA")
            student_id = get_input(stdscr, 2, "Enter Student ID: ", "GPA.txt")

            if student_id in students:
                gpa = students[student_id].calculateGPA()
                gpa = math.floor(gpa * 10) / 10
                display_message(stdscr, 4, f"GPA: {gpa}")
                with open("GPA.txt", 'a') as file:
                    file.write("GPA: " + gpa + '\n')
            else:
                display_message(stdscr, 4, "Student not found.")
            stdscr.getch()
        
        elif choice == ord('5'):
            # List Students
            clear_screen(stdscr)
            display_message(stdscr, 0, "Students")
            # Sort students by GPA in descending order
            sorted_students = sorted(students.items(), key=lambda item: item[1].calculateGPA(), reverse=True)
            for i, (id, student) in enumerate(sorted_students, start=2):
                display_message(stdscr, i, f"{id}: {student.name} - GPA: {student.calculateGPA()}")
            stdscr.getch()

        elif choice == ord('6'):
            # List Courses
            clear_screen(stdscr)
            display_message(stdscr, 0, "Courses")
            for i, (id, name) in enumerate(courses.items(), start=2):
               display_message(stdscr, i, f"{id}: {name}")
            stdscr.getch()
        
        elif choice == ord('7'):
            # Exit
            break

# Run the application
curses.wrapper(main)
