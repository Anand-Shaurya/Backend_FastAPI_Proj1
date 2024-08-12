import json
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    adm_no: int
    dept: str



@app.get("/students/")
async def get_student(adm_no: Optional[int] = None):
    with open("jk.json", "r") as file:
        student_file= json.load(file)
    students = student_file["student_list"]
    if adm_no:
        for i in students:
            if i["adm_no"] == adm_no:
                return i
    else:
        return students

@app.post("/students/")
async def get_student(student: Student):
    try:
        with open("jk.json", "r") as file:
            student_file= json.load(file)
    except FileNotFoundError:
        student_file = {"student_list": []}

            
    students = student_file["student_list"]
    for i in students:
        if i["adm_no"] == student.adm_no:
            raise HTTPException(status_code=401, detail="Student already registered")

    students.append(student.dict())
    student_file["student_list"] = students

    with open("jk.json", "w") as file: 
        json.dump(student_file, file, indent=4)

    return student

@app.put("/students/")
async def get_student(student: Student):
    try:
        with open("jk.json", "r") as file:
            student_file= json.load(file)
    except FileNotFoundError:
        student_file = {"student_list": []}

            
    students = student_file["student_list"]
    flag = True
    for i in students:
        if i["adm_no"] == student.adm_no:
            i["name"] = student.name
            i["adm_no"] = student.adm_no
            i["dept"] = student.dept
            flag = False
            break
    if flag:    
        raise HTTPException(status_code=401, detail="Student not registered")

    student_file["student_list"] = students

    with open("jk.json", "w") as file: 
        json.dump(student_file, file, indent=4)

    return student

@app.delete("/students/{adm_no}")
async def get_student(adm_no):
    try:
        with open("jk.json", "r") as file:
            student_file= json.load(file)
    except FileNotFoundError:
        student_file = {"student_list": []}

            
    students = student_file["student_list"]
    flag = True

    for i in range(len(students)):
        # print(students[i]["adm_no"], adm_no)
        if str(students[i]["adm_no"]) == str(adm_no):
            flag = False
            student = students.pop(i)
            # print(flag, student)
            break
    
                    
    if flag:    
        raise HTTPException(status_code=401, detail="Student not registered")

    student_file["student_list"] = students

    with open("jk.json", "w") as file: 
        json.dump(student_file, file, indent=4)

    return student



