from fastapi import FastAPI
import json
import os

app = FastAPI()

FILE_NAME = "data.json"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

# Read data from JSON file
def read_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Write data to JSON file
def write_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

@app.get("/")
def home():
    return {"message": "Student Management API"}

@app.get("/students")
def get_students():
    return read_data()

@app.post("/students")
def add_student(student: dict):
    students = read_data()
    students.append(student)
    write_data(students)

    return {
        "message": "Student added successfully",
        "student": student
    }

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict):
    students = read_data()

    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student
            write_data(students)

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students = read_data()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            write_data(students)

            return {"message": "Student deleted successfully"}

    return {"message": "Student not found"}