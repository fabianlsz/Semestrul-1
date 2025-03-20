from movie_menu import ui_movie_menu
from user_menu import ui_user_menu
from watchlist_menu import ui_watchlist_menu


def main():
    while True:
        print("\n1. Gestionare utilizatori")
        print("2. Gestionare filme")
        print("3. Gestionare lista de vizionare")
        print("4. Iesi")

        choice = input("Alege o optiune: ")

        if choice == "1":
            ui_user_menu()
        elif choice == "2":
            ui_movie_menu()
        elif choice == "3":
            ui_watchlist_menu()
        elif choice == "4":
            print("Iesire din aplicatie")
            break
        else:
            print("Optiune invalida!")


if __name__ == "__main__":
    main()