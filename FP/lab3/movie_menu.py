from movie_repositories import load_movies, save_movies, add_movies, delete_movies


def ui_movie_menu():
    movies = load_movies()
    while True:
        print("\n1. Adauga film")
        print("2. Sterge film")
        print("3. Actualizeaza rating IMDB")
        print("4. Afiseaza lista de filme")
        print("5. Iesi")

        choice = input("Alege o optiune: ")
        if choice == "1":
            name = input("Numele filmului: ")
            release_date = input("Data lansarii (zz-ll-aaaa): ")
            imdb_score = float(input("Rating IMDB: "))
            actors = input("Actori (separati prin ;): ").split(";")
            add_movies(movies, name, release_date, imdb_score, actors)
            print(f"Filmul {name} a fost adaugat cu succes.")

        elif choice == "2":
            name = input("Numele filmului care va fi sters: ")
            if delete_movies(movies, name):
                print(f"Filmul {name} a fost sters cu succes.")
            else:
                print(f"Filmul cu numele {name} nu a fost gasit.")

        elif choice == "3":
            name = input("Filmul pentru care se actualizeaza rating-ul: ")
            found = False
            for movie in movies:
                if movie["name"] == name:
                    scor_nou = float(input("Noul rating IMDB: "))
                    if scor_nou > 10 or scor_nou < 0:
                        raise ValueError(
                            "Rating-ul IMDB nu poate sa fie mai mic decat 0, sau mai mare decat 10!"
                        )
                    else:
                        movie["imdb_score"] = scor_nou
                        save_movies(movies)
                        print(f"Rating-ul pentru {name} a fost actualizat cu succes!")
                        found = True
                        break
            if not found:
                print(f"Filmul {name} nu a fost gasit.")

        elif choice == "4":
            print("\nLista filmelor:")
            for movie in movies:
                print(
                    f"- {movie['name']}, an aparitie: {movie['release_date']}, IMDB: {movie['imdb_score']}, actori: {', '.join(movie['actors'])}"
                )

        elif choice == "5":
            break
        else:
            print("Optiune invalida.")