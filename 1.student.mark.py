#Build a student mark management system

listMarks = []
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
#input marks for student in this course
def input_marks():
    while True:
        course_ID = input("Enter course ID: ")
        if course_ID not in [course[0] for course in course_list]:
            print("Invalid course ID")
            continue
        break
    marks = int(input("Enter marks: "))
    return course_ID, marks
d = []
#list all courses
course_list = []
def listCourses():
    for course in course_list:
        print(f"Course ID: {course[0]} Course name: {course[1]}")
#list all students
student_list = []
def listStudents():
    for student in student_list:
        print(f"Student ID: {student[0]} Student name: {student[1]} Student date of birth: {student[2]}")
if __name__ == "__main__":
    student_number = get_student_number()
    for i in range(int(student_number)):
        student_name, student_ID, student_DoB = get_student_details()
        student_list.append((student_ID, student_name, student_DoB))
    course_number = get_course_number()
    for i in range(int(course_number)):
        course_name, course_ID = get_course_details()
        course_list.append((course_ID, course_name))
    while True:
        print("\n1. Enter marks for student in course")
        print("2. List all courses")
        print("3. List all students")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            course_ID, marks = input_marks()
            listMarks.append((course_ID, marks))
        elif choice == "2":
            listCourses()
        elif choice == "3":
            listStudents()
        elif choice == "4":
            break
        else:
            print("Invalid choice")