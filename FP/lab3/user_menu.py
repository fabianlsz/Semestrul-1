from user_repositories import load_users, save_user, add_user, delete_user, update_user


def ui_user_menu():
    users = load_users()
    while True:
        print("\n1. Adauga utilizator")
        print("2. Sterge utilizator")
        print("3. Afiseaza utilizatori")
        print("4. Actualizeaza utilizator")
        print("5. Iesi")

        choice = input("Alege o optiune: ")
        if choice == "1":
            name = input("Nume: ")
            age = int(input("Varsta: "))
            add_user(users, name, age)
            print(f"Utilizatorul {name} a fost adaugat cu succes.")

        elif choice == "2":
            name = input("Numele utilizatorului care va fi sters: ")
            if delete_user(users, name):
                print(f"Utilizatorul {name} a fost sters cu succes.")
            else:
                print(f"Utilizatorul cu numele {name} nu a fost gasit.")

        elif choice == "3":
            print("\nLista utilizatorilor:")
            for user in users:
                print(f"- {user['name']}, varsta: {user['age']}")

        elif choice == "4":
            name = input("Nume utilizator pentru actualizare: ")
            new_name = input("Numele actualizat (apasa Enter pentru a nu schimba): ")
            try:
                new_age = input(
                    "Varsta actualizata (apasa Enter pentru a nu schimba): "
                )
                new_age = int(new_age) if new_age else None
            except ValueError:
                print("Varsta trebuie sa fie un numar intreg.")
                continue
            if update_user(users, name, new_name if new_name else None, new_age):
                print(f"Utilizatorul {name} a fost actualizat cu succes.")
            else:
                print(f"Utilizatorul cu numele {name} nu a fost gasit.")

        elif choice == "5":
            break
        else:
            print("Optiune invalida.")