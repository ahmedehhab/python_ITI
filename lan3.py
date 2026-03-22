# def generate_files():
#     f_students = open("students.txt", "w")
#     f_students.write("1,Ahmed Ali\n2,Sara Mohamed\n3,Omar Hassan")
#     f_students.close()

#     f_grades = open("grades.txt", "w")
#     f_grades.write("1,Python,85\n1,Math,90\n2,Python,78\n3,Python,92\n3,Math,88")
#     f_grades.close()
# generate_files()    
############################################################################################
# def display_student_names():
#     f = open("students.txt", "r")
#     for line in f:
#         stu = line.strip().split(",")
#         print(stu[1])
#     f.close()
#     print()
# display_student_names()
###################################################################################33
# def display_python_grades():
#     f = open("grades.txt", "r")
#     lines = f.readlines()
#     f.close()
    
#     python_data = []
#     for line in lines:
#         if "Python" in line:
#             record = line.strip().split(",")
#             python_data.append(record)
    
#     for record in python_data:
#         sid, subject, grade = record
#         print(f"{sid}: {subject} = {grade}")
#     print()

# display_python_grades()   
##########333333333333333333333333333333333333333333333333333333333333333333333333333333333

def search_student_data():
    target_id = input("Enter a student_id to search: ") 
    student_name = "Not Found"
    f_s = open("students.txt", "r") 
    for line in f_s:
        parts = line.strip().split(",")
        if parts[0] == target_id:
            student_name = parts[1]
            break
    f_s.close() 
    
    if student_name == "Not Found":
        print("Student ID not found.")
        return

    print(f"\nStudent Name: {student_name}") 
    
    f_g = open("grades.txt", "r") 
    student_grades = []
    for line in f_g:
        parts = line.strip().split(",")
        if parts[0] == target_id:
            student_grades.append(parts)
    f_g.close() 
    
    total_score = 0
    count_index = 1
    
    for record in student_grades:
        subject = record[1]
        grade = record[2]
        
        print(f"{count_index}. {subject}: {grade}") 
        
        total_score += int(grade)
        count_index += 1
    
    number_of_subjects = len(student_grades)
    if number_of_subjects > 0:
        avg = total_score / number_of_subjects
        print(f"Average Grade: {avg}")

search_student_data()