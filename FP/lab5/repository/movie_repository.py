from domain.movie_domain import Movie
from datetime import datetime

class MovieRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = []
        self.__load()

    def __save(self, movies):
        with open(self.file_path, "w") as file:
            for movie in movies:
                actors = ";".join(movie.actors)
                file.write(f"{movie.movie_id},{movie.title},{movie.release_date.strftime('%d-%m-%Y')},{movie.imdb_rating},{actors}\n")

    def __load(self):
        movies = []
        try:
            with open(self.file_path, "r") as file:
                self.movies = [
                    Movie(
                        int(movie_id),
                        title,
                        datetime.strptime(release_date, "%d-%m-%Y"),
                        float(imdb_rating),
                        [actor for actor in actors.split(";") if actor]
                    )
                    for line in file
                    for movie_id, title, release_date, imdb_rating, actors in [line.strip().split(",")]
                ]
        except FileNotFoundError:
            self.movies = movies

    def get_all(self):
        return self.movies

    def gen_id_movies(self):
        return max((movie.movie_id for movie in self.movies), default=0) + 1

    def find(self, movie_id):
        result = list(filter(lambda movie: movie.movie_id == movie_id, self.movies))
        return self.movies.index(result[0]) if result else -1

    def add(self, movie: Movie):
        if self.find(movie.movie_id) != -1:
            raise ValueError("The movie already exists!")
        self.movies.append(movie)
        self.__save(self.movies)

    def update(self, movieupdated: Movie):
        pos = self.find(movieupdated.movie_id)
        if pos == -1:
            raise ValueError("The movie with the given id doesn't exist!")
        self.movies[pos] = movieupdated
        self.__save(self.movies)

    def delete(self, idMovie: int):
        pos = self.find(idMovie)
        if pos == -1:
            raise ValueError("The movie with the given id doesn't exist!")
        del self.movies[pos]
        self.__save(self.movies)

