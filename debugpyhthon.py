import json

def get_student(adm_no):
    with open("jk.json", "r") as file:
        student_file= json.load(file)
    students = student_file["student_list"]
    for i in students:
        if i["adm_no"] == adm_no:
            return i


a = get_student(2)
print(a)