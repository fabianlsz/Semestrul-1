from domain.movie_domain import Movie
from domain.user_domain import User
from domain.watchlist_domain import Watchlist


class Validation:
    def validator_user(self, user: User):
        erori = ""
        if user.name == "":
            erori += "Name is invalid! "
        if user.age == "":
            erori += "Age is invalid! "
        if len(erori) > 0:
            raise ValueError(erori)

    def validator_movie(self, movie: Movie):
        erori = ""
        if movie.title == "":
            erori += "Title is invalid!"
        if movie.actors == "":
            erori += "Invalid actors!"
        if movie.release_date == "":
            erori+= "Release date is invalid!"
        if movie.imdb_rating == "" or movie.imdb_rating < 1.0 or movie.imdb_rating > 10.0:
            erori+= "IMdB rating is invalid!"
        if len(erori) > 0:
            raise ValueError(erori)

    def validator_watchlist(self, watchlist: Watchlist):
        errors = ""
        if watchlist.user_id is None or watchlist.user_id <= 0:
            errors += "Invalid user ID! "
        if not watchlist.movie_id or not all(isinstance(movieid, int) and movieid > 0 for movieid in watchlist.movie_id):
            errors += "Invalid movie IDs! "
        if len(errors) > 0:
            raise ValueError(errors)