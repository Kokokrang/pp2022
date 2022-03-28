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
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printDetails(self):
        print(f"Name: {self.name} Date of birth: {self.age}")
@property
def name(self):
    return self.name
class student(person):
    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_ID = student_ID
@classmethod
def studentDetails(cls, name, age, student_ID):
    return cls(name, age, student_ID)
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
#driver
if __name__ == "__main__":
    students = inputStudents()
    courses = inputCourses()
    for i in range(students):
        student_name, student_ID, student_DoB = input("Enter student details: ")
        listStudents.append((student_ID, student_name, student_DoB))
    for i in range(courses):
        course_name, course_ID = input("Enter course details: ")
        listCourses.append((course_ID, course_name))
    while True:
        print("\n1. Enter marks for student in course")
        print("2. List all courses")
        print("3. List all students")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                course_ID = input("Enter course ID: ")
                if course_ID not in [course[0] for course in listCourses]:
                    print("Invalid course ID")
                    continue
                break
            marks = int(input("Enter marks: "))
            listMarks.append((student_ID, course_ID, marks))
        elif choice == 2:
            for course in listCourses:
                print(f"Course ID: {course[0]} Course name: {course[1]}")
        elif choice == 3:
            for student in listStudents:
                print(f"Student ID: {student[0]} Student name: {student[1]} Student date of birth: {student[2]}")
        elif choice == 4:
            break
        else:
            print("Invalid choice")
    for student in listStudents:
        for course in listCourses:
            for mark in listMarks:
                if student[0] == mark[0] and course[0] == mark[1]:
                    print(f"Student ID: {student[0]} Course ID: {course[0]} Marks: {mark[2]}")
    print("\nEnd of program")