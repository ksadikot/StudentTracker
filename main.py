
import sys
import Student
import Course

#workflow:

#list of students
studentList = []

#list of courses
courseList = []

#greet user



#add student
    #initStudent with ID name and contact info
#input student grade 
    # get name of student from user
    # get student object
    # get course name
    # check if course exists 
        # if yes then enroll student
        # if no then create course then enroll student

def helpInput():
    print("Here are a list of all commands:")
    print("create student - create a new student reqs(id, name, contact info)")
    print("create course -- create a new course reqs(id, name)")
    print("add grade -- input student grade reqs(course name, student name, course grade)")
    print("enrol student -- enroll a student to a course reqs(course name, student name)")
    print("help -- list all available commands")
    print("exit -- exits program")
    
def createStudent():
    name = input("Enter students name:")
    id = input("Enter student id:")
    contactInfo = input("Enter students contact information:")
    newStudent = Student.Student(name, id, contactInfo)
    studentList.append(newStudent)

def createCourse():
    name = input("Enter course name:")
    id = input("Enter course ID:")

    courseList.append(Course.Course(name, id))

def addGrade():
    studentName = input("Enter students name: ")
    student = getStudent(studentName)
    if student is None:
        return
    courseName = input("Enter course name: ")
    course = getCourse(courseName)
    if course is None:
        return
    grade = input("Enter students grade: ")
    student.inputGrade(grade, courseName)
    course.enrollStudent(student)
    

def getStudent(searchName) -> Student:
    for student in studentList:
        if student.name == searchName:
            return student        
    else:
        print(f"{searchName} does not exist yet, please create student first")
        return None

def getCourse(searchName) -> Course:
    for course in courseList:
        if course.name == searchName:
            return course
    else:
        print(f"{searchName} does not exist yet, please create course first")
        return None

def greetUser():
    print("Welcome to Student Success where students succeed")

def getuserInput():
    return input("There are a list of command available type help for info: ")

def default():
    print("Command not found, type help for command list")

def processCommand(command):
    commandCase = {
        'help': helpInput,
        'create student': createStudent,
        'create course': createCourse,
        'add grade': addGrade,
        'exit': sys.exit
    }

    commandCase.get(command, default)()


greetUser()
while True:
    userInput = getuserInput()
    processCommand(userInput)
