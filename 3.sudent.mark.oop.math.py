
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
    marks_i = math.floor(marks)
    return course_ID, marks_i
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
#driver
if __name__ == "__main__":
    student_number = get_student_number()
    for i in range(student_number):
        student = Student.student_details()
        listStudents.append(student)
    course_number = get_course_number()
    for i in range(course_number):
        course = Course.course_details()
        listCourses.append(course)
    while True:
        course_ID, marks = get_marks()
        if course_ID not in [course[0] for course in listCourses]:
            print("Invalid course ID")
            continue
        listMarks.append((course_ID, marks))
        print("Do you want to add another mark? (y/n)")
        answer = input()
        if answer == "n":
            break
    list_marks()
    GPA = calculate_average()
    print(f"GPA: {GPA}")