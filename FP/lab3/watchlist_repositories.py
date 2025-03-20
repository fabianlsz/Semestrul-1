watchlist_file = "C:/Users/Fabian/Desktop/FP/lab3/watchlist.txt"
from movie_repositories import load_movies

#######################################################################################################
#                           '"watchlist_file = watchlist.txt ----- nu merge???"'                      #
#######################################################################################################

movies = load_movies()


def load_watchlist():
    """Functia incarca lista de filme vizionate de un utilizator din fisierul watchlist.txt

    Returns
    -------
    list
        Returneaza lista de dictionare cu watchlist-ul unui utilizator
    """
    watchlist = []
    try:
        with open(watchlist_file, "r") as file:
            for line in file:
                user_name, movie_name = line.strip().split(",")
                watchlist.append({"user_name": user_name, "movie_name": movie_name})
    except FileNotFoundError:
        print("File not found")
    return watchlist


def save_watchlist(watchlist):
    """Functia salveaza watchlist-ul utilizatorilor

    Parameters
    ----------
    watchlist : list
        Lista de dictionare cu watchlist-ul utilizatorilor
    """
    with open(watchlist_file, "w") as file:
        for entry in watchlist:
            file.write(f"{entry['user_name']},{entry['movie_name']}\n")


def add_to_watchlist(watchlist, user_name, movie_name):
    """Functia adauga un film vizionat in watchlist-ul unui utilizator

    Parameters
    ----------
    watchlist : list
        Lista de dictionare cu filmele vizionate de catre utilizatori
    user_name : string
        Numele utilizatorului caruia ii va fi adaugat filmul in lista de filme vizionate
    movie_name : string
        Numele filmului vizionat de catre utilizator
    """
    with open(watchlist_file, "w") as file:
        watchlist.append({"user_name": user_name, "movie_name": movie_name})
        save_watchlist(watchlist)


def search_actor(movies, actor_name):
    return [movie["name"] for movie in movies if actor_name in movie["actors"]]


def filter_rating(movies, rating_min):
    return [movie["name"] for movie in movies if movie["imdb_score"] >= rating_min]


############################################################################################################
"nu avem nevoie de delete_watchlist, odata ce te-ai uitat la un film de ce l-ai mai sterge de pe watchlist?"
############################################################################################################

# def delete_watchlist(watchlist, user_name):
#     user_found = False
#     for i in range(len(watchlist)):
#         if watchlist[i]["name"] == user_name:
#             del watchlist[i]
#             user_found = True
#             save_watchlist(watchlist)
#             break
#     return user_found