from datetime import datetime
from domain.movie_domain import Movie
from repository.movie_repository import MovieRepository
from service.service_movies import service_movies
from domain.validation import Validation

def show_movie_menu():
    print("\nMovie Management Menu:")
    print("1. Show all movies")
    print("2. Add a movie")
    print("3. Remove a movie")
    print("4. Update a movie")
    print("5. Exit")

def show_all_movies(service_movie):
    movies = service_movie.get_movies()
    if not movies:
        print("No movies available.")
    else:
        for movie in movies:
            release_date = movie.release_date.strftime('%d-%m-%Y')
            print(f"ID: {movie.movie_id}, Title: {movie.title}, Release Date: {release_date}, IMDb: {movie.imdb_rating}, Actors: {', '.join(movie.actors)}")

def add_movie(service_movie):
    try:
        title = input("Enter movie title: ")
        release_date_str = input("Enter release date (dd-mm-yyyy): ")
        release_date = datetime.strptime(release_date_str, '%d-%m-%Y')
        imdb_rating = float(input("Enter IMDb rating: "))
        actors = input("Enter actors (comma-separated): ").split(",")
        service_movie.add_movie(title, release_date, imdb_rating, [actor.strip() for actor in actors])
        print("Movie added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_movie(service_movie):
    try:
        movie_id = int(input("Enter movie ID to remove: "))
        service_movie.remove_movie(movie_id)
        print("Movie removed successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def update_movie(service_movie):
    try:
        movie_id = int(input("Enter movie ID to update: "))
        movie_to_update = next((movie for movie in service_movie.get_movies() if movie.movie_id == movie_id), None)

        if not movie_to_update:
            print("Movie not found!")
            return

        title = input(f"Enter new title (current: {movie_to_update.title}): ")
        title = title if title else movie_to_update.title

        release_date_str = input(
            f"Enter new release date (current: {movie_to_update.release_date.strftime('%d-%m-%Y')}): ")
        release_date = movie_to_update.release_date
        if release_date_str:
            release_date = datetime.strptime(release_date_str, "%d-%m-%Y")

        imdb_rating_str = input(f"Enter new IMDb rating (current: {movie_to_update.imdb_rating}): ")
        imdb_rating = movie_to_update.imdb_rating
        if imdb_rating_str:
            imdb_rating = float(imdb_rating_str)

        actors_input = input(f"Enter new actors (current: {', '.join(movie_to_update.actors)}): ")
        actors = movie_to_update.actors
        if actors_input:
            actors = [actor.strip() for actor in actors_input.split(";")]

        updated_movie = Movie(movie_id, title, release_date, imdb_rating, actors)
        service_movie.update_movie(updated_movie)
        print("Movie updated successfully!")

    except ValueError as e:
        print(f"Error: {e}")

def movie_menu():
    file_path = "movies.txt"
    validator = Validation()
    movie_repository = MovieRepository(file_path)
    service_movie = service_movies(validator, movie_repository)

    while True:
        show_movie_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_movies(service_movie)
        elif choice == "2":
            add_movie(service_movie)
        elif choice == "3":
            remove_movie(service_movie)
        elif choice == "4":
            update_movie(service_movie)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")