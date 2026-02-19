from data import classes, students

def create_class():
    class_id = input("Entrez l'ID de la classe : ")
    if class_id in classes:
        print("Cette classe existe déjà !")
        return
    name = input("Entrez le nom de la classe : ")
    classes[class_id] = {"name": name, "students": []}
    print(f"La classe '{name}' a été créée !")

def delete_class():
    class_id = input("Entrez l'ID de la classe à supprimer : ")
    if class_id not in classes:
        print("Classe non trouvée !")
        return
    for student_id in classes[class_id]["students"]:
        students[student_id]["class_id"] = None
    del classes[class_id]
    print(" Classe supprimée !")

def list_classes():
    if not classes:
        print("Aucune classe disponible.")
        return
    print("\nListe des classes :")
    for cid, c in classes.items():
        print(f"{cid} : {c['name']} ({len(c['students'])} étudiants)")

def class_details():
    class_id = input("Entrez l'ID de la classe : ")
    if class_id not in classes:
        print("Classe non trouvée !")
        return
    c = classes[class_id]
    print(f"\n Nom : {c['name']}")
    print(f"Nombre d’étudiants : {len(c['students'])}")
    if c['students']:
        print("Liste des étudiants :")
        for sid in c['students']:
            s = students.get(sid)
            if s:
                print(f" - {sid} : {s['first_name']} {s['last_name']}")
            else:
                print(f" - {sid} : (données manquantes)")
    else:
        print("Aucun étudiant inscrit.")
