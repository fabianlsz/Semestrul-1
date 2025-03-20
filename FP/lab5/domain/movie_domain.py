from datetime import datetime

class Movie:
    def __init__(self, movie_id, title, release_date, imdb_rating, actors):
        self.movie_id = movie_id
        self.title = title
        if not isinstance(release_date, datetime):
            raise ValueError("release_date must be a datetime object")
        self._release_date = release_date
        self.imdb_rating = imdb_rating
        self.actors = actors

    @property
    def release_date(self):
        return self._release_date
    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, value):
        self._actors = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def imdb_rating(self):
        return self._imdb_rating

    @imdb_rating.setter
    def imdb_rating(self, value):
        self._imdb_rating = value

    def __str__(self):
        release_date_str = self.release_date.strftime("%d-%m-%Y")
        return f"Movie[ID={self.movie_id}, Title={self.title}, Release Date={release_date_str}, IMDb Rating={self.imdb_rating}, Actors={self.actors}]"