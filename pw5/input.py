from curses import wrapper
import math
import numpy
listMarks = []
listStudents = []
listCourses = []
list_credits = []

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
    def __init__(self, course_ID, course_name, credits):
        self.course_ID = course_ID
        self.course_name = course_name
        self.credits = credits
    @classmethod
    def course_details(cls):
        course_name = input("Enter course name: ")
        course_ID = input("Enter course ID: ")
        credits = int(input("Enter course credits: "))
        return cls(course_ID, course_name, credits)
    def __getitem__(self, item):
        return self.course_ID
    def list_courses(self):
        print(f"Course ID: {self.course_ID} Course name: {self.course_name}")
def get_marks():
    while True:
        course_ID = input("Enter course ID: ")
        if course_ID not in [course[0] for course in listCourses]:
            print("Invalid course ID")
            continue
        break
    marks = float(input("Enter marks: "))
    marks = math.round(marks, 1)
    return course_ID, marks
def list_marks():
    for course_ID, marks in listMarks:
        print(f"Course ID: {course_ID} Marks: {marks}")
        
#sum(marks * credits) / sum(credits)
def calculate_average():
    sum_credits = 0
    sum_marks = 0
    for course_ID, marks in listMarks:
        for course in listCourses:
            if course_ID == course[0]:
                sum_credits += int(course[2])
                sum_marks += marks * int(course[2])
    average = sum_marks / sum_credits
    average = numpy.round(average, 1)
    return average

#Sort student list by GPA descending
def sort_student_list():
    list_students = []
    for student in listStudents:
        list_students.append(student.student_name)
    list_students.sort(reverse=True)
    return list_students

#Write student info to students.txt after finishing input
f = open("students.txt", "w")
f.write("Student ID\tStudent name\tStudent date of birth\n")
f.close()
f = open("students.txt", "r")
print(f.read())

#Write course info to courses.txt after finishing input
f = open("courses.txt", "w")
f.write("Course ID\tCourse name\tCredits\n")
f.close()
f = open("courses.txt", "r")
print(f.read())

#Write marks to marks.txt after finishing input
f = open("marks.txt", "w")
f.write("Course ID\tMarks\n")
f.close()
f = open("marks.txt", "r")
print(f.read())
