import os
import zlib
import json
from domains.student import Student

def compress_files():
    data = {
        'students': [],
        'courses': [],
        'marks': []
    }

    # Read and compress data
    with open("students.txt", 'r') as file:
        for line in file:
            id, name, dob = line.strip().split(',')
            data['students'].append({'id': id, 'name': name, 'dob': dob})

    with open("courses.txt", 'r') as file:
        for line in file:
            id, name = line.strip().split(',')
            data['courses'].append({'id': id, 'name': name})

    with open("marks.txt", 'r') as file:
        for line in file:
            student_id, course_id, mark, credit = line.strip().split(',')
            data['marks'].append({'student_id': student_id, 'course_id': course_id, 'mark': float(mark), 'credit': float(credit)})

    # Convert the data to a JSON string
    data_str = json.dumps(data)

    # Compress the data
    compressed_data = zlib.compress(data_str.encode('utf-8'))

    # Write the compressed data to students.dat
    with open("students.dat", 'wb') as file:
        file.write(compressed_data)

    print("Files compressed successfully.")

def decompress_and_load_data(students, courses):
    if os.path.exists("students.dat"):
        print("Decompressing and loading data from students.dat...")
        with open("students.dat", 'rb') as file:
            compressed_data = file.read()
        decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
        data = json.loads(decompressed_data)

        # Load students data
        for student_data in data['students']:
            students[student_data['id']] = Student(student_data['id'], student_data['name'], student_data['dob'])

        # Load courses data
        for course_data in data['courses']:
            courses[course_data['id']] = course_data['name']

        # Load marks data
        for mark_data in data['marks']:
            student_id = mark_data['student_id']
            course_id = mark_data['course_id']
            mark = mark_data['mark']
            credit = mark_data['credit']
            students[student_id].add_mark(course_id, mark, credit)

        print("Data loaded successfully.")
    else:
        print("students.dat not found. Starting with empty data.")