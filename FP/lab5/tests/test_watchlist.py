from domain.validation import Validation
from domain.watchlist_domain import Watchlist
from repository.watchlist_repository import WatchlistRepository
from repository.movie_repository import MovieRepository
from repository.user_repository import UserRepository
from domain.movie_domain import Movie
from domain.user_domain import User
from service.service_watchlist import ServiceWatchlist
from datetime import datetime

def test_add_watchlist():
    test_file_path = "test_watchlists.txt"
    validator = Validation()
    repo_watchlist = WatchlistRepository(test_file_path)
    repo_movie = MovieRepository("test_movies.txt")
    repo_user = UserRepository("test_users.txt")

    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    user = User(repo_user.gen_id_user(), "Test User", 30)
    repo_user.add(user)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie = Movie(repo_movie.gen_id_movies(), "Test Movie", release_date, 8.5, ["Actor 1", "Actor 2"])
    repo_movie.add(movie)

    service.add_watchlist(user.user_id, [movie.movie_id])
    all_watchlists = repo_watchlist.get_all()

    assert len(all_watchlists) == 1
    assert all_watchlists[0].user_id == user.user_id
    assert movie.movie_id in all_watchlists[0].movie_id

def test_get_all_watchlists():
    test_file_path = "test_watchlists.txt"
    cleanup([test_file_path, "test_movies.txt", "test_users.txt"])  # Clear files at the start

    validator = Validation()
    repo_watchlist = WatchlistRepository(test_file_path)
    repo_movie = MovieRepository("test_movies.txt")
    repo_user = UserRepository("test_users.txt")

    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    user2 = User(repo_user.gen_id_user(), "User 2", 30)
    repo_user.add(user2)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie1 = Movie(repo_movie.gen_id_movies(), "Movie 1", release_date, 7.0, ["Actor A"])
    repo_movie.add(movie1)

    service.add_watchlist(user2.user_id, [movie1.movie_id])

    all_watchlists = repo_watchlist.get_all()

    assert len(all_watchlists) == 1
    assert all_watchlists[0].user_id == user2.user_id

    cleanup([test_file_path, "test_movies.txt", "test_users.txt"])

def test_remove_watchlist():
    test_file_path = "test_watchlists.txt"
    validator = Validation()
    repo_watchlist = WatchlistRepository(test_file_path)
    repo_movie = MovieRepository("test_movies.txt")
    repo_user = UserRepository("test_users.txt")

    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    user = User(repo_user.gen_id_user(), "Test User", 30)
    repo_user.add(user)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie = Movie(repo_movie.gen_id_movies(), "Test Movie", release_date, 8.5, ["Actor 1", "Actor 2"])
    repo_movie.add(movie)

    service.add_watchlist(user.user_id, [movie.movie_id])
    all_watchlists = repo_watchlist.get_all()
    assert len(all_watchlists) == 1

    service.remove_watchlist(all_watchlists[0].watchlist_id)
    all_watchlists = repo_watchlist.get_all()
    assert len(all_watchlists) == 0

    cleanup([test_file_path, "test_movies.txt", "test_users.txt"])

def test_update_watchlist():
    test_file_path = "test_watchlists.txt"
    validator = Validation()
    repo_watchlist = WatchlistRepository(test_file_path)
    repo_movie = MovieRepository("test_movies.txt")
    repo_user = UserRepository("test_users.txt")

    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    user = User(repo_user.gen_id_user(), "Test User", 30)
    repo_user.add(user)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie1 = Movie(repo_movie.gen_id_movies(), "Movie 1", release_date, 8.5, ["Actor 1", "Actor 2"])
    movie2 = Movie(repo_movie.gen_id_movies(), "Movie 2", release_date, 7.0, ["Actor A"])
    repo_movie.add(movie1)

    service.add_watchlist(user.user_id, [movie1.movie_id])
    all_watchlists = repo_watchlist.get_all()
    watchlist_to_update = all_watchlists[0]

    updated_watchlist = Watchlist(watchlist_to_update.watchlist_id, user.user_id, [movie2.movie_id])
    repo_watchlist.update(updated_watchlist)

    all_watchlists = repo_watchlist.get_all()
    assert len(all_watchlists) == 1
    assert movie2.movie_id in all_watchlists[0].movie_id

    cleanup([test_file_path, "test_movies.txt", "test_users.txt"])

def test_count_movies_by_actor():
    test_file_path_movies = "test_movies.txt"
    test_file_path_watchlists = "test_watchlists.txt"
    test_file_path_users = "test_users.txt"


    repo_movie = MovieRepository(test_file_path_movies)
    repo_watchlist = WatchlistRepository(test_file_path_watchlists)
    repo_user = UserRepository(test_file_path_users)
    validator = Validation()
    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie1 = Movie(repo_movie.gen_id_movies(), "Movie 1", release_date, 7.5, ["Actor A", "Actor B"])
    repo_movie.add(movie1)

    count = service.count_movies_by_actor("Actor A")
    assert count == 1

    count = service.count_movies_by_actor("Actor Z")
    assert count == 0

    cleanup([test_file_path_movies, test_file_path_watchlists, test_file_path_users])

def test_average_rating_by_actor():
    test_file_path_movies = "test_movies.txt"
    test_file_path_watchlists = "test_watchlists.txt"
    test_file_path_users = "test_users.txt"

    # Set up repositories and service
    repo_movie = MovieRepository(test_file_path_movies)
    repo_watchlist = WatchlistRepository(test_file_path_watchlists)
    repo_user = UserRepository(test_file_path_users)
    validator = Validation()
    service = ServiceWatchlist(validator, repo_watchlist, repo_movie, repo_user)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    movie1 = Movie(repo_movie.gen_id_movies(), "Movie 1", release_date, 7.5, ["Actor A"])
    repo_movie.add(movie1)

    average_rating = service.average_rating_by_actor("Actor A")
    assert abs(average_rating - 7.75) < 10.1

    average_rating = service.average_rating_by_actor("Actor Z")
    assert average_rating == 0

    cleanup([test_file_path_movies, test_file_path_watchlists, test_file_path_users])


def cleanup(file_paths):
    import os
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    test_add_watchlist()
    print("test_add_watchlist passed")
    test_get_all_watchlists()
    print("test_get_all_watchlists passed")
    test_remove_watchlist()
    print("test_remove_watchlist passed")
    test_update_watchlist()
    print("test_update_watchlist passed")
    test_count_movies_by_actor()
    print("test_count_movies_by_actor passed")
    test_average_rating_by_actor()
    print("test_average_rating_by_actor passed")