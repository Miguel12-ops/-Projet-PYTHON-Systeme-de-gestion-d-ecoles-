from data import students, classes
from data import grades

def create_student():
    student_id = input("Entrez l'ID de l’étudiant : ")
    if student_id in students:
        print(" Cet étudiant existe déjà !")
        return
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    email = input("Email : ")
    students[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "class_id": None
    }
    print(f"Étudiant {first_name} {last_name} créé !")

def add_student_to_class():
    student_id = input("ID de l’étudiant : ")
    if student_id not in students:
        print("Étudiant non trouvé !")
        return
    class_id = input("ID de la classe : ")
    if class_id not in classes:
        print(" Classe non trouvée !")
        return
    if student_id in classes[class_id]['students']:
        print(" Étudiant déjà dans cette classe !")
        return
    classes[class_id]['students'].append(student_id)
    students[student_id]['class_id'] = class_id
    print(f"Étudiant ajouté à la classe {classes[class_id]['name']}")

def remove_student_from_class():
    student_id = input("ID de l’étudiant : ")
    if student_id not in students:
        print("Étudiant non trouvé !")
        return
    class_id = students[student_id]['class_id']
    if not class_id:
        print(" Cet étudiant n’appartient à aucune classe.")
        return
    classes[class_id]['students'].remove(student_id)
    students[student_id]['class_id'] = None
    print(" Étudiant retiré de la classe.")

def list_students_of_class():
    class_id = input("ID de la classe : ")
    if class_id not in classes:
        print("Classe non trouvée !")
        return
    if not classes[class_id]['students']:
        print("Aucun étudiant dans cette classe.")
        return
    print(f"\nÉtudiants de la classe {classes[class_id]['name']} :")
    for sid in classes[class_id]['students']:
        s = students[sid]
        print(f" - {sid} : {s['first_name']} {s['last_name']} ({s['email']})")

def student_details():
    student_id = input("ID de l’étudiant : ")
    if student_id not in students:
        print(" Étudiant non trouvé !")
        return
    s = students[student_id]
    print(f"\n Nom : {s['first_name']} {s['last_name']}")
    print(f"Email : {s['email']}")
    print(f"Classe : {s['class_id'] if s['class_id'] else 'Aucune'}")

def add_grade():
    student_id = input("ID de l’étudiant : ")
    if student_id not in students:
        print(" Étudiant non trouvé !")
        return
    try:
        note = float(input("Entrez la note (0-20) : "))
    except ValueError:
        print("La note doit être un nombre !")
        return
    if note < 0 or note > 20:
        print("La note doit être entre 0 et 20 !")
        return
    if student_id not in grades:
        grades[student_id] = []
    grades[student_id].append(note)
    print(f"Note ajoutée à {students[student_id]['first_name']} {students[student_id]['last_name']}.")

def student_average():
    student_id = input("ID de l’étudiant : ")
    if student_id not in students:
        print("Étudiant non trouvé !")
        return
    if student_id not in grades or len(grades[student_id]) == 0:
        print("Cet étudiant n’a pas de notes.")
        return
    avg = sum(grades[student_id]) / len(grades[student_id])
    print(f"Moyenne de {students[student_id]['first_name']} {students[student_id]['last_name']} : {avg:.2f}/20")

def class_average():
    class_id = input("ID de la classe : ")
    if class_id not in classes:
        print("Classe non trouvée !")
        return
    total = 0
    count = 0
    for student_id in classes[class_id]['students']:
        if student_id in grades and len(grades[student_id]) > 0:
            total += sum(grades[student_id])
            count += len(grades[student_id])
    if count == 0:
        print("Aucun étudiant de cette classe n’a de notes.")
        return
    avg = total / count
    print(f"Moyenne de la classe {classes[class_id]['name']} : {avg:.2f}/20")

