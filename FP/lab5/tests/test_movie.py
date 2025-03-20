from domain.movie_domain import Movie
from datetime import datetime
from domain.validation import Validation
from repository.movie_repository import MovieRepository
from service.service_movies import service_movies


class Bataiedejoc2(Validation):
    def validator_movie(self, movie: Movie):
        if not isinstance(movie.title, str) or movie.title == "":
            raise ValueError("Movie title is required")


def test_add_movie():
    test_file_path = "test_movies.txt"
    validator = Bataiedejoc2()
    repo = MovieRepository(test_file_path)
    service = service_movies(validator, repo)
    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Movie1", release_date, 8.5, ["Actor 1"])

    all_movies = repo.get_all()

    assert len(all_movies) == 1
    assert all_movies[0].title == "Movie1"
    assert all_movies[0].imdb_rating == 8.5
    assert "Actor 1" in all_movies[0].actors

    cleanup(test_file_path)


def test_get_all_movies():
    test_file_path = "test_movies.txt"
    validator = Bataiedejoc2()
    repo = MovieRepository(test_file_path)
    service = service_movies(validator, repo)

    release_date1 = datetime.strptime("01-01-2020", "%d-%m-%Y")
    release_date2 = datetime.strptime("01-01-2021", "%d-%m-%Y")

    service.add_movie("Movie1", release_date1, 8.5, ["Actor 1"])
    service.add_movie("Movie2", release_date2, 8.5, ["Actor 2"])

    all_movies = repo.get_all()

    assert len(all_movies) == 2
    assert all_movies[0].title == "Movie1"
    assert all_movies[1].title == "Movie2"

    cleanup(test_file_path)


def test_remove_movie():
    test_file_path = "test_movies.txt"
    validator = Bataiedejoc2()
    repo = MovieRepository(test_file_path)
    service = service_movies(validator, repo)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Movie1", release_date, 8.5, ["Actor 1"])

    all_movies = repo.get_all()
    assert len(all_movies) == 1

    service.remove_movie(all_movies[0].movie_id)
    all_movies = repo.get_all()
    assert len(all_movies) == 0
    cleanup(test_file_path)


def test_update_movie():
    test_file_path = "test_movies.txt"
    validator = Bataiedejoc2()
    repo = MovieRepository(test_file_path)
    service = service_movies(validator, repo)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Movie1", release_date, 8.5, ["Actor 1"])

    all_movies = repo.get_all()
    movie_to_update = all_movies[0]

    updated_movie = Movie(movie_to_update.movie_id, "Updated Movie", release_date, 9.0, ["Actor 3"])
    repo.update(updated_movie)

    all_movies = repo.get_all()

    assert len(all_movies) == 1
    assert all_movies[0].title == "Updated Movie"
    assert all_movies[0].imdb_rating == 9.0
    assert "Actor 3" in all_movies[0].actors

    cleanup(test_file_path)


def cleanup(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    test_add_movie()
    print("test_add_movie passed")
    test_get_all_movies()
    print("test_get_all_movies passed")
    test_remove_movie()
    print("test_remove_movie passed")
    test_update_movie()
    print("test_update_movie passed")