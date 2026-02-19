from classes import create_class, delete_class, list_classes, class_details

def main_menu():
    while True:
        print("\n= GESTION DES CLASSES =")
        print("1. Créer une classe")
        print("2. Supprimer une classe")
        print("3. Lister toutes les classes")
        print("4. Détails d'une classe")
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
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main_menu()
