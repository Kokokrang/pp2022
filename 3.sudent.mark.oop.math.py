import math
import numpy
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
        print("\n1. Enter marks for student in course")
        print("2. List all courses")
        print("3. List all students")
        print("4. List all marks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            course_ID, marks = get_marks()
            listMarks.append((course_ID, marks))
        elif choice == 2:
            for course in listCourses:
                course.list_courses()
        elif choice == 3:
            for student in listStudents:
                student.list_student()
        elif choice == 4:
            list_marks()
        elif choice == 5:
            break
        else:
            print("Invalid choice")