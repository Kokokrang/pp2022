#Build a student mark management system

from this import d
from prompt_toolkit import prompt
from sympy import re

def get_student_number():
    student_number = input("Enter student number: ")
    return student_number
#get student details
def get_student_details():
    student_name = input("Enter student name: ")
    student_ID = input("Enter student ID: ")
    student_DoB = input("Enter student date of birth: ")
    return student_name, student_ID, student_DoB
#get course number
def get_course_number():
    course_number = input("Enter course number: ")
    return course_number
#get course details
def get_course_details():
    course_name = input("Enter course name: ")
    course_ID = input("Enter course ID: ")
    return course_name, course_ID
#select a course, input marks for student in this course
course_list = []
def inputMarks():
    while True:
        course_ID = input("Enter course ID: ")
        if course_ID not in [course[0] for course in course_list]:
            print("Bad course ID")
            continue
        break
    marks = int(input("Enter marks: "))
    if course_ID in d:
        d[course_ID].append((student_ID, marks))
    else:
        d[course_ID] = [(student_ID, marks)]
        
#list all courses
def listCourses():
    for course in course_list:
        print(f"Course ID: {course[0]} Course name: {course[1]}")
#list all students
def listStudents():
    for student in student_list:
        print(f"Student ID: {student[0]} Student name: {student[1]} Student date of birth: {student[2]}")
#driver
def main():
    while True:
        print("\n1. Enter student details")
        print("2. Enter course details")
        print("3. Enter marks for student in course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_name, student_ID, student_DoB = get_student_details()
            student_list.append((student_ID, student_name, student_DoB))
        elif choice == 2:
            course_name, course_ID = get_course_details()
            course_list.append((course_ID, course_name))
        elif choice == 3:
            inputMarks()
        elif choice == 4:
            listCourses()
        elif choice == 5:
            listStudents()
        elif choice == 6:
            break
        else:
            print("Invalid choice")