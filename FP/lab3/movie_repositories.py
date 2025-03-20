movie_file = "C:/Users/Fabian/Desktop/FP/lab3/movies.txt"

#######################################################################################################
#                           '"movie_file = movie.txt ----- nu merge???"'                              #
#######################################################################################################


def load_movies():
    """Functia incarca filmele stocate in fisierul movies.txt

    Returns
    -------
    list
        Returneaza lista de dictionare cu filme
    """
    movies = []
    try:
        with open(movie_file, "r") as file:
            for line in file:
                parts = line.strip().split(",", 3)
                if len(parts) == 4:
                    name = parts[0].strip()
                    release_date = parts[1].strip()
                    imdb_score = float(parts[2].strip())
                    actors = parts[3].strip().split(";")
                    movies.append(
                        {
                            "name": name,
                            "release_date": release_date,
                            "imdb_score": imdb_score,
                            "actors": actors,
                        }
                    )
    except FileNotFoundError:
        print("File not found")
    return movies


def save_movies(movies):
    """Functia salveaza un film nou in fisierul movies.txt

    Parameters
    ----------
    movies : list
        Lista actualizata cu filme
    """
    with open(movie_file, "w") as file:
        for movie in movies:
            file.write(
                f"{movie['name']},{movie['release_date']},{movie['imdb_score']},{';'.join(movie['actors'])}\n"
            )


def add_movies(movies, name, release_date, imdb_score, actors):
    """Functia adauga filme in lista movies.txt

    Parameters
    ----------
    movies : list
        lista de dictionare cu filme
    name : string
        Numele filmului care va fi adaugat
    release_date : string
        Data de lansare a filmului
    imdb_score : float
        Nota IMDB acordata filmului
    actors : string
        Actorii principali ai filmului
    """
    if imdb_score < 0 or imdb_score > 10:
        raise ValueError(
            "Rating-ul IMDB nu poate sa fie mai mic decat 0, sau mai mare decat 10!"
        )
    movies.append(
        {
            "name": name,
            "release_date": release_date,
            "imdb_score": imdb_score,
            "actors": actors,
        }
    )
    save_movies(movies)


def delete_movies(movies, name):
    """Functia sterge filme din fisierul movies.txt

    Parameters
    ----------
    movies : list
        Lista de dictionare cu filme
    name : string
        Numele filmului care va fii sters

    Returns
    -------
    list
        Lista cu filmele actualizate dupa stergere
    """
    movie_found = False
    for i in range(len(movies)):
        if movies[i]["name"] == name:
            del movies[i]
            movie_found = True
            save_movies(movies)
            break
    return movie_found