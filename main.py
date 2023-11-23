
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
        # if no - exit out of command and tell user to create course
        # if yes - continue
    # get grade of student
    # add course and grade to students transcript
    # enroll student

def helpInput():
    print("Here are a list of all commands:")
    print("create student - create a new student reqs(id, name, contact info)")
    print("create course -- create a new course reqs(id, name)")
    print("add grade -- input student grade reqs(course name, student name, course grade)")
    print("enrol student -- enroll a student to a course reqs(course name, student name)")
    print("help -- list all available commands")
    print("exit -- exits program")
    
def listStudents():
    for student in studentList:
        print(f'{student.name}')
    pass

def addStudent():
    name = input("Enter students name:")
    id = input("Enter student id:")
    contactInfo = input("Enter students contact information:")
    studentList.append(Student.Student(name, id, contactInfo))
    print("Successfully added student")

def addCourse():
    name = input("Enter course name:")
    id = input("Enter course ID:")
    courseList.append(Course.Course(name, id))
    print("Successfully added course")

def addGrade():
    studentName = input("Enter students name: ")
    student = getStudent(studentName)
    if student is None:
        response = input()
        if response == 'Y' or response == 'y':
            addStudent()
            student = getStudent(studentName)
        else:
            return

    courseName = input("Enter course name: ")
    while (courseName != 'quit'):
        course = getCourse(courseName)
        if course is None:
            response = input()
            if response == 'Y' or response == 'y':
                addCourse()
                course = getCourse(courseName)
                
            else:
                return 
        
        grade = input("Enter students grade: ")
        student.inputGrade(grade, courseName)
        course.enrollStudent(student)
        print('Successfully added grade for student')
        courseName = input("Enter course name: ")
    

def getStudent(searchName) -> Student:
    for student in studentList:
        if student.name == searchName:
            return student        
    else:
        print(f"{searchName} does not exist yet, would you like to add this student? (Y/N): ")
        return None

def getCourse(searchName) -> Course:
    for course in courseList:
        if course.name == searchName:
            return course
    else:
        print(f"{searchName} does not exist yet, would you like to add this course? (Y/N):")
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
        'add student': addStudent,
        'add course': addCourse,
        'add grade': addGrade,
        'list students': listStudents,
        'exit': sys.exit
    }

    commandCase.get(command, default)()


greetUser()
while True:
    userInput = getuserInput()
    processCommand(userInput)
