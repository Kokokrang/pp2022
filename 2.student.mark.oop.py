from itertools import count
listMarks = []
listStudents = []
listCourses = []
#input number of students
def inputStudents():
    while True:
        students = int(input("Enter number of students: "))
        if students < 1:
            print("Invalid number of students")
            continue
        break
    return students
#input number of courses
def inputCourses():
    while True:
        courses = int(input("Enter number of courses: "))
        if courses < 1:
            print("Invalid number of courses")
            continue
        break
    return courses
#inheritance
class person:
    count = 0
    def __init__(self, name, DoB):
        self.name = name
        self.DoB = DoB
    def printDetails(self):
        print(f"Name: {self.name} Date of birth: {self.DoB}")
@property
def name(self):
    return self.name
@classmethod
def getCount(cls):
    return cls.count
class student(person):
    def __init__(self, name, DoB, student_ID):
        super().__init__(name, DoB)
        self.student_ID = student_ID
        student.count += 1
    def printDetails(self):
        super().printDetails()
        print(f"Student ID: {self.student_ID}")
class course:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def printDetails(self):
        print(f"Course ID: {self.ID} Course name: {self.name}")
class marks:
    def __init__(self, student_ID, course_ID, marks):
        self.student_ID = student_ID
        self.course_ID = course_ID
        self.marks = marks
    def printDetails(self):
        print(f"Student ID: {self.student_ID} Course ID: {self.course_ID} Marks: {self.marks}")
if __name__ == "__main__":
    students = inputStudents()
    courses = inputCourses()
    #input student details
    for i in range(students):
        name, DoB, student_ID = input("Enter student details: ").split()
        listStudents.append(student(name, DoB, student_ID))
    #input course details
    for i in range(courses):
        name, ID = input("Enter course details: ").split()
        listCourses.append(course(name, ID))
    #input marks for student in course
    for i in range(students):
        student_ID = listStudents[i].student_ID
        for j in range(courses):
            course_ID = listCourses[j].ID
            marks = int(input("Enter marks: "))
            listMarks.append(marks(student_ID, course_ID, marks))
    #list all courses
    for i in range(courses):
        listCourses[i].printDetails()
    #list all students
    for i in range(students):
        listStudents[i].printDetails()
    #list all marks
    for i in range(students):
        for j in range(courses):
            listMarks[i*courses+j].printDetails()
    #list all students in a course
    for i in range(courses):
        for j in range(students):
            listMarks[j*courses+i].printDetails()
    #list all courses of a student
    for i in range(students):
        for j in range(courses):
            listMarks[i*courses+j].printDetails()
    #list all students in a course
    for i in range(courses):
        for j in range(students):
            listMarks[j*courses+i].printDetails()
    #list all courses of a student
    for i in range(students):
        for j in range(courses):
            listMarks[i*courses+j].printDetails()
    #list all students in a course