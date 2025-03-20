from movie_repositories import load_movies, save_movies, add_movies, delete_movies


def test_add_movies():
    original_movies = load_movies()

    try:
        test_movies = original_movies.copy()

        test_name = "Interstellar"
        test_release_date = "2014"
        test_imdb_score = 8.6
        test_actors = ["Matthew McConaughey"]

        add_movies(
            test_movies, test_name, test_release_date, test_imdb_score, test_actors
        )

        assert any(
            movie["name"] == test_name and movie["imdb_score"] == test_imdb_score
            for movie in test_movies
        ), "Filmul 'Interstellar' nu a fost adaugat in lista"

    finally:
        save_movies(original_movies)
        print("Movies file restored.")


def test_delete_movies():
    original_movies = load_movies()

    try:
        test_movies = original_movies.copy()

        test_name_to_add = "Salahara"
        test_release_date = "2010"
        test_imdb_score = 8.8
        test_actors = ["Leonardo"]
        add_movies(
            test_movies,
            test_name_to_add,
            test_release_date,
            test_imdb_score,
            test_actors,
        )

        deleted = delete_movies(test_movies, test_name_to_add)

        assert deleted == True, "Filmul 'Salahara' ar fi trebuit sa fie sters"
        assert not any(
            movie["name"] == test_name_to_add for movie in test_movies
        ), "Filmul 'Salahara' nu ar mai trebui sa fie in lista"
    finally:
        save_movies(original_movies)
        print("Movies file restored.")


def test_save_movies():
    original_movies = load_movies()

    try:
        test_movies = [
            {
                "name": "The Dark Knight",
                "release_date": "2008",
                "imdb_score": 9.0,
                "actors": ["Christian Bale"],
            }
        ]

        save_movies(test_movies)

        loaded_movies = load_movies()
        assert (
            len(loaded_movies) == 1
        ), "Lista de filme ar trebui sa contina o singura intrare"
        assert (
            loaded_movies[0]["name"] == "The Dark Knight"
            and loaded_movies[0]["imdb_score"] == 9.0
        ), "Datele filmului sunt incorecte"
    finally:
        save_movies(original_movies)
        print("Movies file restored.")


test_add_movies()
test_delete_movies()
test_save_movies()

print("Toate testele au fost trecute cu succes!")