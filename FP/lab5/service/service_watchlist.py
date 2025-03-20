from functools import reduce
from domain.validation import Validation
from domain.watchlist_domain import Watchlist
from repository.watchlist_repository import WatchlistRepository
from repository.movie_repository import MovieRepository
from repository.user_repository import UserRepository


class ServiceWatchlist:
    def __init__(self, validator: Validation, repoWatchlist: WatchlistRepository, repoMovieRepository: MovieRepository, repoUserRepository: UserRepository):
        self.Validator = validator
        self.WatchlistRepository = repoWatchlist
        self.MovieRepository = repoMovieRepository
        self.UserRepository = repoUserRepository

    def add_watchlist(self, user_id: int, movie_id: list):
        for watchlist in self.WatchlistRepository.get_all():
            if watchlist.user_id == user_id or watchlist.movie_id == movie_id:
                raise ValueError("The watchlist already exists for this user!")
        new_watchlist_id = self.WatchlistRepository.gen_id_watchlist()
        new_watchlist = Watchlist(new_watchlist_id, user_id, movie_id)
        self.Validator.validator_watchlist(new_watchlist)
        self.WatchlistRepository.add(new_watchlist)

    def remove_watchlist(self, watchlist_id: int):
        self.WatchlistRepository.delete(watchlist_id)

    def update_watchlist(self, updatedWatchlist: Watchlist):
        self.WatchlistRepository.update(updatedWatchlist)

    def get_watchlists(self):
        return self.WatchlistRepository.get_all()

    def filter_movies_by_actor(self, actor: str):
        movies = self.MovieRepository.get_all()
        return list(filter(lambda m: actor in m.actors, movies ))

    def filter_movies_by_rating(self, rating: float):
        movies = self.MovieRepository.get_all()
        return list(filter(lambda m: m.imdb_rating > rating, movies))

    def count_movies_by_actor(self, actor: str):
        movies = self.MovieRepository.get_all()
        return sum(map(lambda m: actor in m.actors, movies))

    def average_rating_by_actor(self, actor: str):
        movies = self.MovieRepository.get_all()
        relevant_movies = list(filter(lambda m: actor in m.actors, movies))
        total_rating = reduce(lambda acc, m: acc + m.imdb_rating, relevant_movies, 0)
        return total_rating / len(relevant_movies) if relevant_movies else 0