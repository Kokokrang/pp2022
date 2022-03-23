#create class student
class Student:
    def __init__(self, student_ID, student_name, student_DoB):
        self.student_ID = student_ID
        self.student_name = student_name
        self.student_DoB = student_DoB
    def __str__(self):
        return f"Student ID: {self.student_ID} Student name: {self.student_name} Student date of birth: {self.student_DoB}"
#create class course
class Course:
    def __init__(self, course_ID, course_name):
        self.course_ID = course_ID
        self.course_name = course_name
    def __str__(self):
        return f"Course ID: {self.course_ID} Course name: {self.course_name}"
#create class marks
class Marks:
    def __init__(self, course_ID, student_ID, marks):
        self.course_ID = course_ID
        self.student_ID = student_ID
        self.marks = marks
    def __str__(self):
        return f"Course ID: {self.course_ID} Student ID: {self.student_ID} Marks: {self.marks}"


