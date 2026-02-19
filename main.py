from classes import create_class, delete_class, list_classes, class_details, general_stats
from students import create_student, add_student_to_class, remove_student_from_class, list_students_of_class, \
    student_details, add_grade, student_average, class_average


def main_menu():
    while True:
        print("\n=== GESTION DE L’ÉCOLE ===")
        print("1. Créer une classe")
        print("2. Supprimer une classe")
        print("3. Lister toutes les classes")
        print("4. Détails d'une classe")
        print("5. Créer un étudiant")
        print("6. Ajouter un étudiant à une classe")
        print("7. Retirer un étudiant d'une classe")
        print("8. Lister les étudiants d'une classe")
        print("9. Détails d'un étudiant")
        print("10. Ajouter une note à un étudiant")
        print("11. Moyenne d'un étudiant")
        print("12. Moyenne d'une classe")
        print("13. Statistiques générales")
        print("0. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            create_class()
        elif choice == "2":
            delete_class()
        elif choice == "3":
            list_classes()
        elif choice == "4":
            class_details()
        elif choice == "5":
            create_student()
        elif choice == "6":
            add_student_to_class()
        elif choice == "7":
            remove_student_from_class()
        elif choice == "8":
            list_students_of_class()
        elif choice == "9":
            student_details()
        elif choice == "10":
            add_grade()
        elif choice == "11":
            student_average()
        elif choice == "12":
            class_average()
        elif choice == "13":
            general_stats()
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main_menu()
