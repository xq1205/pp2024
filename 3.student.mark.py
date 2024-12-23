import math
import numpy as np

class Student:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

class Course:
    def __init__(self, ID, name, credits):
        self.ID = ID
        self.name = name
        self.credits = credits

class Mark:
    def __init__(self, mark):
        self.mark = mark

def floor_mark(mark):
    return math.floor(mark * 10) / 10

def calculate_gpa(student, course_list):
    weighted_sum = 0
    total_credits = 0
    for mark, course in zip(student.marks, course_list):
        weighted_sum += mark * course.credits
        total_credits += course.credits
    return weighted_sum / total_credits

def sort_students_by_gpa(student_list, course_list):
    student_gpa = [(student, calculate_gpa(student, course_list)) for student in student_list]
    sorted_students = sorted(student_gpa, key=lambda x: x[1], reverse=True)
    return [student[0] for student in sorted_students]

def main():
    nb_student = int(input("Input number of students: "))
    student_list = []
    for i in range(nb_student):
        student_id = input(f"Input ID of student {i+1}: ")
        student_name = input(f"Input name of student {i+1}: ")
        student_dob = input(f"Input the birth date of student {i+1}: ")
        student_list.append(Student(student_id, student_name, student_dob))
        
    nb_course = int(input("Input number of courses: "))
    course_list = []
    for j in range(nb_course):
        course_id = input(f"Input ID of course {j+1}: ")
        course_name = input(f"Input name of course {j+1}: ")
        course_credits = float(input(f"Input number of credits for course {j+1}: "))
        course_list.append(Course(course_id, course_name, course_credits))
        
    for student in student_list:
        for course in course_list:
            mark = float(input(f"Input mark of {course.name} for student {student.name}: "))
            student.add_mark(floor_mark(mark))
    
    sorted_students = sort_students_by_gpa(student_list, course_list)

    print("Sorted student list by GPA descending:")
    for student in sorted_students:
        print(f"Student name: {student.name}, ID: {student.ID}, GPA: {calculate_gpa(student, course_list):.2f}")

if __name__ == "__main__":
    main()
