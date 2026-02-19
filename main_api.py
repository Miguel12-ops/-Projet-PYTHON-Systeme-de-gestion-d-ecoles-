from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from data import classes, students, grades

app = FastAPI(title="School Management API")

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API School Management"}



# ---------- SCHEMAS ----------
class ClassBase(BaseModel):
    name: str

class ClassResponse(ClassBase):
    id: str
    students: List[str] = []

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class StudentResponse(StudentBase):
    id: str
    class_id: Optional[str] = None

class GradeRequest(BaseModel):
    value: float

# ---------- CLASSES ----------
@app.post("/classes", response_model=ClassResponse)
def create_class_api(id: str, class_data: ClassBase):
    if id in classes:
        raise HTTPException(status_code=400, detail="Classe déjà existante")
    classes[id] = {"name": class_data.name, "students": []}
    return {"id": id, "name": class_data.name, "students": []}

@app.get("/classes", response_model=List[ClassResponse])
def list_classes_api():
    return [{"id": cid, "name": c["name"], "students": c["students"]} for cid, c in classes.items()]

@app.get("/classes/{id}", response_model=ClassResponse)
def class_details_api(id: str):
    if id not in classes:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    c = classes[id]
    return {"id": id, "name": c["name"], "students": c["students"]}

@app.delete("/classes/{id}")
def delete_class_api(id: str):
    if id not in classes:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    # Supprimer les étudiants de cette classe
    for student_id in classes[id]["students"]:
        students[student_id]["class_id"] = None
    del classes[id]
    return {"message": "Classe supprimée"}

# ---------- STUDENTS ----------
@app.post("/students", response_model=StudentResponse)
def create_student_api(id: str, student_data: StudentBase):
    if id in students:
        raise HTTPException(status_code=400, detail="Étudiant déjà existant")
    students[id] = {
        "first_name": student_data.first_name,
        "last_name": student_data.last_name,
        "email": student_data.email,
        "class_id": None
    }
    return {"id": id, "first_name": student_data.first_name, "last_name": student_data.last_name, "email": student_data.email, "class_id": None}

@app.post("/classes/{class_id}/students/{student_id}")
def add_student_to_class_api(class_id: str, student_id: str):
    if class_id not in classes:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    if student_id in classes[class_id]["students"]:
        raise HTTPException(status_code=400, detail="Étudiant déjà dans cette classe")
    classes[class_id]["students"].append(student_id)
    students[student_id]["class_id"] = class_id
    return {"message": "Étudiant ajouté à la classe"}

@app.delete("/classes/{class_id}/students/{student_id}")
def remove_student_from_class_api(class_id: str, student_id: str):
    if class_id not in classes:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    if student_id not in students or student_id not in classes[class_id]["students"]:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé dans cette classe")
    classes[class_id]["students"].remove(student_id)
    students[student_id]["class_id"] = None
    return {"message": "Étudiant retiré de la classe"}

@app.get("/students/{student_id}", response_model=StudentResponse)
def student_details_api(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    s = students[student_id]
    return {"id": student_id, "first_name": s["first_name"], "last_name": s["last_name"], "email": s["email"], "class_id": s["class_id"]}

# ---------- NOTES ----------
@app.post("/students/{student_id}/grades")
def add_grade_api(student_id: str, grade: GradeRequest):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    if student_id not in grades:
        grades[student_id] = []
    grades[student_id].append(grade.value)
    return {"message": "Note ajoutée"}

@app.get("/students/{student_id}/average")
def student_average_api(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    if student_id not in grades or len(grades[student_id]) == 0:
        raise HTTPException(status_code=404, detail="Pas de notes pour cet étudiant")
    avg = sum(grades[student_id])/len(grades[student_id])
    return {"student_id": student_id, "average": round(avg, 2)}

@app.get("/classes/{class_id}/average")
def class_average_api(class_id: str):
    if class_id not in classes:
        raise HTTPException(status_code=404, detail="Classe non trouvée")
    total = 0
    count = 0
    for student_id in classes[class_id]["students"]:
        if student_id in grades and len(grades[student_id]) > 0:
            total += sum(grades[student_id])
            count += len(grades[student_id])
    if count == 0:
        return {"class_id": class_id, "average": None}
    avg = total / count
    return {"class_id": class_id, "average": round(avg, 2)}

# ---------- STATISTIQUES ----------
@app.get("/stats")
def general_stats_api():
    total_classes = len(classes)
    total_students = len(students)
    total_students_with_grades = sum(1 for s in students if s in grades and len(grades[s]) > 0)
    return {
        "total_classes": total_classes,
        "total_students": total_students,
        "students_with_grades": total_students_with_grades
    }
