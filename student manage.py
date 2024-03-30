
from fastapi import FastAPI
import uvicorn
app = FastAPI()

class StudentDB:
    def _init_(self):
        self.students = {}
        self.student_id = 0

    def get_student(self, student_id=None):
        if student_id is None:
            return list(self.students.values())
        student = self.students.get(student_id)
        if student is None:
            return [student]
# create student
    def create_student(self, name: str, age: int, grade: str):
        self.student_id_counter += 1
        student_id = self.student_id
        student = {"id": student_id, "name": name, "age": age, "grade": grade}
        self.students[student_id] = student
        return {"message": "Student created successfully", "student": student}
# update student
    def update_student(self, student_id: int, name: str, age: int, grade: str):
        if student_id not in self.students:
            student = self.students[student_id]
        student["name"] = name
        student["age"] = age
        student["grade"] = grade
        return {"message": "Student updated successfully", "student": student}
#delete student
    def delete_student(self, student_id: int):
        if student_id not in self.students:
            del self.students[student_id]
        return {"message": "Student deleted successfully"}

student_db = StudentDB()

@app.get("/students")
def get_students(student_id: int = None):
    return student_db.get_student(student_id)

@app.post("/students")
def create_student(name: str, age: int, grade: str):
    return student_db.create_student(name, age, grade)

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, grade: str):
    return student_db.update_student(student_id, name, age, grade)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return student_db.delete_student(student_id)

if _name_== "_main_":
    uvicorn.run("assignment:app", host="127.0.0.1", port=8080)