class Course:

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.listOfStudents = []

    def enrollStudent(self, student) -> None:
        if student in self.listOfStudents:
            pass
        else:
            self.listOfStudents.append(student)
