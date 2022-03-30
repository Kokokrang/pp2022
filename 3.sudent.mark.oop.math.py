#Use math module to round-down student scores to 1-digit decimal upon input
import math
import numpy as np
listMarks = []
listStudents = []
listCourses = []
#input number of students
def get_student_number():
    student_number = int(input("Enter number of students: "))
    return student_number
class Student:
    def __init__(self, student_ID, student_name, student_DoB):
        self.student_ID = student_ID
        self.student_name = student_name
        self.student_DoB = student_DoB
    @classmethod
    def student_details(cls):
        student_name = input("Enter student name: ")
        student_ID = input("Enter student ID: ")
        student_DoB = input("Enter student date of birth: ")
        return cls(student_ID, student_name, student_DoB)
    def list_student(self):
        print(f"Student ID: {self.student_ID} Student name: {self.student_name} Student date of birth: {self.student_DoB}")
def get_course_number():
    course_number = int(input("Enter number of courses: "))
    return course_number
class Course:
    def __init__(self, course_ID, course_name):
        self.course_ID = course_ID
        self.course_name = course_name
    @classmethod
    def course_details(cls):
        course_name = input("Enter course name: ")
        course_ID = input("Enter course ID: ")
        return cls(course_ID, course_name)
    def list_courses(self):
        print(f"Course ID: {self.course_ID} Course name: {self.course_name}")
def get_marks():
    while True:
        course_ID = input("Enter course ID: ")
        if course_ID not in [course[0] for course in listCourses]:
            print("Invalid course ID")
            continue
        break
    marks = int(input("Enter marks: "))
    return course_ID, marks
