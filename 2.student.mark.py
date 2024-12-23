class Student:
    def __init__(self, ID, name, dob):
        self.ID=ID
        self.name=name
        self.dob=dob
class Course:
    def __init__(self, ID, name):
        self.ID=ID
        self.name=name
nb_student=int(input("Input number of student: "))
student_list=[]
for i in range(nb_student):
    student_id=input(f"Input ID of student {i+1}: ")
    student_name=input(f"Input name of student {i+1}: ")
    student_dob=input(f"Input the birth date of student {i+1}: ")
    student_list.append(Student(student_id,student_name,student_dob))

nb_course=int(input("Input number of course: "))
course_list=[]
mark_list=[]
for j in range(nb_course):
    course_id=input(f"Input ID of course {j+1}: ")
    course_name=input(f"Input name of course {j+1}: ")
    course_list.append(Course(course_id,course_name))
    mark_list.append(j)
for k in range(nb_course):
    select=input("Select a course by type the ID: ")
    mark_list[k]=[]
    for m in range(nb_course):
        if select==course_list[m].ID:
            for n in range(nb_student):
                mark=input(f"Input {course_list[m].name}'s mark of {student_list[n].name}: ")
                mark_list[m].append(mark)
print("Student list: ")
for p in range(len(student_list)):
    print(f"Name: {student_list[p].name}. Student ID: {student_list[p].ID}. Student dob: {student_list[p].dob}")
print("Course list:")
for t in range(len(course_list)):
    print(f"Course ID: {course_list[t].ID}. Code name: {course_list[t].name}")
print(f"Mark of {course_list[0].name}")
for q in range(len(student_list)):
    print(f"Student ID: {student_list[q].ID}. Student name: {student_list[q].name}. Mark: {mark_list[0][q]}")
    

                
                
            





    
    