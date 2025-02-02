class Student:
    def __init__(self, name, studentID, group, gpa, on_internship=None):
        self.gpa = gpa
        self.name = name
        self.group = group 
        self.studentID = studentID
        self.on_internship = on_internship
    
    def display_info(self):
        is_on_internship = ''
        if self.on_internship==True:
            is_on_internship = 'The student is on intership'
        elif self.on_internship == False:
            is_on_internship = 'The student is not on intership'
        else:
            is_on_internship = "No data about student's intership activities"
        return f"Student's name: {self.name}\n" \
               f"Student's ID: {self.studentID}\n" \
               f"Student's group: {self.group}\n" \
               f"Student's gpa: {self.gpa}\n" \
               f"{is_on_internship}"
    
    def is_writing(self):
        return f"{self.name} is writing."
               
               
        
               
