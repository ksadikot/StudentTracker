class Student:
    

    def __init__(self, name, id, contactInfo) -> None:
        self.name = name 
        self.id = id
        self.contactInfo = contactInfo
        self.transcript = {}

    def inputGrade(self, grade, courseName):
        self.transcript[courseName] = grade

    def viewStudent(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Contact Information: " + self.contactInfo)

    def studentTranscript(self):
        for course, grade in self.transcript.items():
            print(f"{course}: {grade}")

        

    
