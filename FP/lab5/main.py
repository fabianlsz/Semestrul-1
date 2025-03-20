from ui.ui_movie import movie_menu
from ui.ui_user import user_menu
from ui.ui_watchlist import watchlist_menu


def show_main_menu():
    print("\nFilm Management Menu:")
    print("1. Access user management menu")
    print("2. Access movie management menu")
    print("3. Access movie watchlist menu")
    print("4. Quit")

def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            movie_menu()
        elif choice == "3":
            watchlist_menu()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()