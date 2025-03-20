from watchlist_repositories import (
    load_watchlist,
    save_watchlist,
    add_to_watchlist,
    search_actor,
    filter_rating,
)
from movie_repositories import load_movies


def ui_watchlist_menu():
    watchlist = load_watchlist()
    movies = load_movies()

    while True:
        print("\n1. Adauga film in lista de vizionare a unui utilizator")
        print("2. Afiseaza filmele vizionate de un utilizator")
        print("3. Cauta filme dupa actor")
        print("4. Filtreaza filmele dupa un anumit rating IMDB ")
        print("5. Iesi")

        choice = input("Alege o optiune: ")

        if choice == "1":
            user_name = input("Numele utilizatorului: ")
            movie_name = input("Numele filmului: ")
            if any(movie["name"] == movie_name for movie in movies):
                add_to_watchlist(watchlist, user_name, movie_name)
                print(
                    f"Filmul {movie_name} a fost adaugat in watchlist-ul utilizatorului {user_name}."
                )
            else:
                print(f"Filmul {movie_name} nu exista in baza de date.")
        elif choice == "2":
            user_name = input("Numele utilizatorului: ")
            user_watchlist = [
                entry["movie_name"]
                for entry in watchlist
                if entry["user_name"] == user_name
            ]
            if user_watchlist:
                print(f"\nFilme vizionate de {user_name}: ")
                for movie_name in user_watchlist:
                    print(f"- {movie_name}")
            else:
                print(f"{user_name} nu are watchlist inregistrat.")
        elif choice == "3":
            actor = input("Numele actorului: ")
            print(search_actor(movies, actor))
        elif choice == "4":
            rating_min = int(input("Nota minima de filtrare: "))
            print(filter_rating(movies, rating_min))
        elif choice == "5":
            break
        else:
            print("Optiune invalida!")