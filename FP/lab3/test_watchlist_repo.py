from watchlist_repositories import (
    load_watchlist,
    save_watchlist,
    add_to_watchlist,
    search_actor,
    filter_rating,
)
from movie_repositories import load_movies, save_movies


def test_add_to_watchlist():
    original_watchlist = load_watchlist()

    try:
        test_watchlist = original_watchlist.copy()

        test_user_name = "Test User"
        test_movie_name = "Test Movie"

        add_to_watchlist(test_watchlist, test_user_name, test_movie_name)

        assert any(
            entry["user_name"] == test_user_name
            and entry["movie_name"] == test_movie_name
            for entry in test_watchlist
        ), "Filmul a fost adaugat cu succes in watchlist."
    finally:
        save_watchlist(original_watchlist)
        print("Watchlist restored.")


def test_search_actor():
    original_movies = load_movies()

    try:
        test_movies = original_movies.copy()

        test_movies.append(
            {
                "name": "Inception",
                "release_date": "2010",
                "imdb_score": 8.8,
                "actors": ["Leonardo DiCaprio"],
            }
        )
        test_movies.append(
            {
                "name": "Dune",
                "release_date": "2021",
                "imdb_score": 8.1,
                "actors": ["Timothee Chalamet"],
            }
        )

        result = search_actor(test_movies, "Leonardo DiCaprio")
        assert (
            len(result) == 1
        ), "Numarul de filme cu Leonardo DiCaprio ar trebui sa fie egal cu 1."
        assert "Inception" in result, "Inception ar trebui sa fie in lista."
        result_no_match = search_actor(test_movies, "Actor Inexistent")
        assert len(result_no_match) == 0, "Nu exista filme pentru acest actor!."

    finally:
        save_movies(original_movies)
        print("Watchlist file restored.")


def test_filter_rating():
    original_movies = load_movies()

    try:
        test_movies = []

        test_movies.append(
            {
                "name": "Inception",
                "release_date": "2010",
                "imdb_score": 8.8,
                "actors": ["Leonardo DiCaprio"],
            }
        )
        test_movies.append(
            {
                "name": "Dune",
                "release_date": "2021",
                "imdb_score": 8.1,
                "actors": ["Timothee Chalamet"],
            }
        )
        test_movies.append(
            {
                "name": "lalalala",
                "release_date": "2025",
                "imdb_score": 6.2,
                "actors": ["miaumiau"],
            }
        )
        result = filter_rating(test_movies, 8.0)

        assert len(result) == 2, "Ar trebui sa fie 2 filme cu rating peste 8.0."
        assert "Inception" in result, "'Inception' ar trebui să fie în listă."
        assert "Dune" in result, "'Dune' ar trebui să fie în listă."

        result_high = filter_rating(test_movies, 9.0)
        assert len(result_high) == 0, "Nu exista filme cu rating peste 9.0."

        result_low = filter_rating(test_movies, 6.0)
        assert len(result_low) == 3, "Ar trebui sa fie 3 filme cu rating peste 6.0."

    finally:
        save_movies(original_movies)
        print("Movies file restored.")


test_filter_rating()
test_search_actor()
test_add_to_watchlist()

print("Toate testele au fost trecute cu succes!")