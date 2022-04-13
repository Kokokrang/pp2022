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
    list_students = sort_student_list()
    print(f"Students: {list_students}")