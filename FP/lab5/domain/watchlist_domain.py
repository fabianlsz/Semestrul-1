class Watchlist:
    def __init__(self, watchlist_id, user_id, movie_id):
        self.watchlist_id = watchlist_id
        self.user_id = user_id
        self.movie_id = movie_id

    @property
    def watchlist_id(self):
        return self._watchlist_id

    @watchlist_id.setter
    def watchlist_id(self, value):
        self._watchlist_id = value

    def __str__(self):
        return f"Watchlist[ID={self.watchlist_id}, UserID={self.user_id}, Movies={self.movie_id}]"