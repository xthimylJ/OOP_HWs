from StudentClass import Student

num_of_Student_obj = int(input('How many students would you like to register? '))
i = 1
students = []
while i <= num_of_Student_obj:
    print(f'\nRegistering student_{i}:')
    name = input('Enter the name of the student: ')
    st_id = input('Enter the ID of the student: ')
    st_group = input('Enter the group of the student: ')
    st_gpa = float(input('Enter the GPA of the student: '))
    internship = None
    on_internship =input('Does the student do any internship? "Yes/No/No data" responses only: ').strip().lower()
    if on_internship == 'yes':
        internship = True
    elif on_internship == 'no':
        internship = False
    else:
        internship = None
    studnt = Student(name, st_id, st_group, st_gpa, internship)
    students.append(studnt)
    i+=1
for i in students:
    print('--------------------')
    print(i.display_info())
    
    


    

