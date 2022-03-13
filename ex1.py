#storing information
students = []
student ={
	"id": None,
	"name": None,
	"DoB": None,
}
#input function
def addStudent():
	student["id"] = input("Enter student id: ")
	student["name"] = input("Enter student name: ")
	student["DoB"] = input("Enter student DoB: ")
	students.append(student)
#list function
def listStudent():
    print("There %s student in the list" % len(students))
    for i in students:
		print("ID: %s, Name: %s, DoB: %s" % (i["id"], i["name"], i["DoB"]))
#driver
if __name__ == "__main__":
    	addStudent()
		listStudent()
#end
