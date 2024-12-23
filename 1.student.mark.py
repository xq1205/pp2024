nb=int(input("Input number of student in class: "))
idStudent_list=[]
nameStudent_list=[]
idCourse_list=[]
dob_list=[]
nameCourse_list=[]
mark_list=[]
for i in range(nb):
    print(f"Input information of student {i+1}: ")
    id_student= input(f"Input the ID of student {i+1}: ")
    idStudent_list.append(id_student)
    name_student=input(f"Input the name of student {i+1}: ")
    nameStudent_list.append(name_student)
    dob=input(f"Input the day of birth of studenr {i+1}: ")
    dob_list.append(dob)
nb_course=int(input(f"Input the number of course: "))
for j in range(nb_course):
    id_course=input(f"Input ID of course {j+1}: ")
    idCourse_list.append(id_course)
    name_course=input(f"Input name of course {j+1}: ")
    nameCourse_list.append(name_course)
    mark_list.append(j)
for o in range(len(mark_list)):
    course=input("Select a course by type the ID: ")
    mark_list[o]=[]
    for k in range(len(idCourse_list)):
        if course==idCourse_list[k]:
            for n in range(nb):
                mark=input(f"Input mark of {nameCourse_list[k]} for {nameStudent_list[n]}: " )
                mark_list[o].append(mark)
print("List of course:")
for l in range(nb_course):
    print(f"Course ID: {idCourse_list[l]}. Course Name: {nameCourse_list[l]}")
print("List student:")
for u in range(nb):
    print(f"Student ID: {idStudent_list[u]}. Student name: {nameStudent_list[u]}. Student DoB: {dob_list[u]}")  
print(f"Mark of {nameCourse_list[0]}:")
for m in range(nb):
    print(f"Student name: {nameStudent_list[m]}. Mark: {mark_list[0][m]}")
        
        
        
    
