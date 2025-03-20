import customtkinter as ctk
from tkinter import simpledialog, messagebox
import json

USER_FILE = 'users.json'
MOVIE_FILE = 'movies.json'
WATCHLIST_FILE = 'watchlists.json'

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

users = load_data(USER_FILE)
movies = load_data(MOVIE_FILE)
watchlists = load_data(WATCHLIST_FILE)

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Menu")
        self.geometry("300x200")

        self.user_button = ctk.CTkButton(self, text="User Menu", command=self.open_user_menu)
        self.user_button.pack(pady=10)

        self.movie_button = ctk.CTkButton(self, text="Movie Menu", command=self.open_movie_menu)
        self.movie_button.pack(pady=10)

        self.watchlist_button = ctk.CTkButton(self, text="Watchlist Menu", command=self.open_watchlist_menu)
        self.watchlist_button.pack(pady=10)

        self.quit_button = ctk.CTkButton(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def open_user_menu(self):
        self.withdraw()
        self.user_menu = UserMenu(self)
        self.user_menu.mainloop()

    def open_movie_menu(self):
        self.withdraw()
        self.movie_menu = MovieMenu(self)
        self.movie_menu.mainloop()

    def open_watchlist_menu(self):
        self.withdraw()
        self.watchlist_menu = WatchlistMenu(self)
        self.watchlist_menu.mainloop()

class UserMenu(ctk.CTk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.title("User Menu")
        self.geometry("300x300")

        self.show_users_button = ctk.CTkButton(self, text="Show All Users", command=self.show_users)
        self.show_users_button.pack(pady=10)

        self.add_user_button = ctk.CTkButton(self, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=10)

        self.delete_user_button = ctk.CTkButton(self, text="Delete User", command=self.delete_user)
        self.delete_user_button.pack(pady=10)

        self.edit_user_button = ctk.CTkButton(self, text="Edit User", command=self.edit_user)
        self.edit_user_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.exit_menu)
        self.exit_button.pack(pady=10)

    def show_users(self):
        if users:
            user_list = "\n".join([f"{user['id']}: {user['name']}, {user['age']}" for user in users])
            messagebox.showinfo("Users", user_list)
        else:
            messagebox.showinfo("Users", "No users available")

    def add_user(self):
        user_id = simpledialog.askinteger("Input", "Enter user ID:")
        user_name = simpledialog.askstring("Input", "Enter user name:")
        user_age = simpledialog.askinteger("Input", "Enter user age:")
        if user_id and user_name and user_age:
            users.append({"id": user_id, "name": user_name, "age": user_age})
            save_data(USER_FILE, users)
            messagebox.showinfo("Add User", f"User '{user_name}' added successfully")

    def delete_user(self):
        user_id = simpledialog.askinteger("Input", "Enter user ID to delete:")
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            users.remove(user)
            save_data(USER_FILE, users)
            messagebox.showinfo("Delete User", f"User '{user['name']}' deleted successfully")
        else:
            messagebox.showinfo("Delete User", f"User with ID '{user_id}' not found")

    def edit_user(self):
        user_id = simpledialog.askinteger("Input", "Enter user ID to edit:")
        user = next((user for user in users if user['id'] == user_id), None)
        if user:
            new_name = simpledialog.askstring("Input", "Enter new user name:", initialvalue=user['name'])
            new_age = simpledialog.askinteger("Input", "Enter new user age:", initialvalue=user['age'])
            if new_name and new_age:
                user['name'] = new_name
                user['age'] = new_age
                save_data(USER_FILE, users)
                messagebox.showinfo("Edit User", f"User '{user_id}' updated successfully")
        else:
            messagebox.showinfo("Edit User", f"User with ID '{user_id}' not found")

    def exit_menu(self):
        self.destroy()
        self.parent.deiconify()

class MovieMenu(ctk.CTk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.title("Movie Menu")
        self.geometry("300x300")

        self.show_movies_button = ctk.CTkButton(self, text="Show All Movies", command=self.show_movies)
        self.show_movies_button.pack(pady=10)

        self.add_movie_button = ctk.CTkButton(self, text="Add Movie", command=self.add_movie)
        self.add_movie_button.pack(pady=10)

        self.remove_movie_button = ctk.CTkButton(self, text="Remove Movie", command=self.remove_movie)
        self.remove_movie_button.pack(pady=10)

        self.update_movie_button = ctk.CTkButton(self, text="Update Movie", command=self.update_movie)
        self.update_movie_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.exit_menu)
        self.exit_button.pack(pady=10)

    def show_movies(self):
        if movies:
            messagebox.showinfo("Movies", "\n".join(movies))
        else:
            messagebox.showinfo("Movies", "No movies available")

    def add_movie(self):
        movie = simpledialog.askstring("Input", "Enter movie title:")
        if movie:
            movies.append(movie)
            save_data(MOVIE_FILE, movies)
            messagebox.showinfo("Add Movie", f"Movie '{movie}' added successfully")

    def remove_movie(self):
        movie = simpledialog.askstring("Input", "Enter movie title to remove:")
        if movie in movies:
            movies.remove(movie)
            save_data(MOVIE_FILE, movies)
            messagebox.showinfo("Remove Movie", f"Movie '{movie}' removed successfully")
        else:
            messagebox.showinfo("Remove Movie", f"Movie '{movie}' not found")

    def update_movie(self):
        old_movie = simpledialog.askstring("Input", "Enter movie title to update:")
        if old_movie in movies:
            new_movie = simpledialog.askstring("Input", "Enter new movie title:")
            if new_movie:
                movies[movies.index(old_movie)] = new_movie
                save_data(MOVIE_FILE, movies)
                messagebox.showinfo("Update Movie", f"Movie '{old_movie}' updated successfully to '{new_movie}'")
        else:
            messagebox.showinfo("Update Movie", f"Movie '{old_movie}' not found")

    def exit_menu(self):
        self.destroy()
        self.parent.deiconify()

class WatchlistMenu(ctk.CTk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.title("Watchlist Menu")
        self.geometry("300x400")

        self.add_to_watchlist_button = ctk.CTkButton(self, text="Add to Watchlist", command=self.add_to_watchlist)
        self.add_to_watchlist_button.pack(pady=10)

        self.show_watchlists_button = ctk.CTkButton(self, text="Show All Watchlists", command=self.show_watchlists)
        self.show_watchlists_button.pack(pady=10)

        self.edit_watchlist_button = ctk.CTkButton(self, text="Edit Watchlist", command=self.edit_watchlist)
        self.edit_watchlist_button.pack(pady=10)

        self.remove_watchlist_button = ctk.CTkButton(self, text="Remove Watchlist", command=self.remove_watchlist)
        self.remove_watchlist_button.pack(pady=10)

        self.filter_by_actor_button = ctk.CTkButton(self, text="Filter Movies by Actor", command=self.filter_by_actor)
        self.filter_by_actor_button.pack(pady=10)

        self.filter_by_rating_button = ctk.CTkButton(self, text="Filter Movies by IMDb Rating", command=self.filter_by_rating)
        self.filter_by_rating_button.pack(pady=10)

        self.count_movies_button = ctk.CTkButton(self, text="Count Movies by Actor", command=self.count_movies)
        self.count_movies_button.pack(pady=10)

        self.calculate_rating_button = ctk.CTkButton(self, text="Calculate IMDb Rating of Actor's Movies", command=self.calculate_rating)
        self.calculate_rating_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.exit_menu)
        self.exit_button.pack(pady=10)

    def add_to_watchlist(self):
        user = simpledialog.askstring("Input", "Enter user name:")
        movie = simpledialog.askstring("Input", "Enter movie title to add to watchlist:")
        if user and movie:
            if user not in watchlists:
                watchlists[user] = []
            watchlists[user].append(movie)
            save_data(WATCHLIST_FILE, watchlists)
            messagebox.showinfo("Add to Watchlist", f"Movie '{movie}' added to {user}'s watchlist")

    def show_watchlists(self):
        if watchlists:
            result = "\n".join([f"{user}: {', '.join(movies)}" for user, movies in watchlists.items()])
            messagebox.showinfo("Watchlists", result)
        else:
            messagebox.showinfo("Watchlists", "No watchlists available")

    def edit_watchlist(self):
        user = simpledialog.askstring("Input", "Enter user name:")
        if user in watchlists:
            old_movie = simpledialog.askstring("Input", f"Enter movie title to replace in {user}'s watchlist:")
            if old_movie in watchlists[user]:
                new_movie = simpledialog.askstring("Input", "Enter new movie title:")
                if new_movie:
                    watchlists[user][watchlists[user].index(old_movie)] = new_movie
                    save_data(WATCHLIST_FILE, watchlists)
                    messagebox.showinfo("Edit Watchlist", f"Movie '{old_movie}' replaced with '{new_movie}' in {user}'s watchlist")
            else:
                messagebox.showinfo("Edit Watchlist", f"Movie '{old_movie}' not found in {user}'s watchlist")
        else:
            messagebox.showinfo("Edit Watchlist", f"User '{user}' not found")

    def remove_watchlist(self):
        user = simpledialog.askstring("Input", "Enter user name to remove watchlist:")
        if user in watchlists:
            del watchlists[user]
            save_data(WATCHLIST_FILE, watchlists)
            messagebox.showinfo("Remove Watchlist", f"Watchlist for '{user}' removed successfully")
        else:
            messagebox.showinfo("Remove Watchlist", f"User '{user}' not found")

    def filter_by_actor(self):
        actor = simpledialog.askstring("Input", "Enter actor name to filter movies:")
        if actor:
            filtered_movies = [movie for movie in movies if actor in movie]
            messagebox.showinfo("Filter by Actor", "\n".join(filtered_movies) if filtered_movies else "No movies found")

    def filter_by_rating(self):
        rating = simpledialog.askstring("Input", "Enter minimum IMDb rating to filter movies:")
        if rating:
            filtered_movies = [movie for movie in movies if float(movie.split()[-1]) >= float(rating)]
            messagebox.showinfo("Filter by IMDb Rating", "\n".join(filtered_movies) if filtered_movies else "No movies found")

    def count_movies(self):
        actor = simpledialog.askstring("Input", "Enter actor name to count movies:")
        if actor:
            count = sum(actor in movie for movie in movies)
            messagebox.showinfo("Count Movies by Actor", f"{actor} appeared in {count} movies")

    def calculate_rating(self):
        actor = simpledialog.askstring("Input", "Enter actor name to calculate IMDb rating:")
        if actor:
            actor_movies = [float(movie.split()[-1]) for movie in movies if actor in movie]
            avg_rating = sum(actor_movies) / len(actor_movies) if actor_movies else 0
            messagebox.showinfo("Calculate IMDb Rating", f"Average IMDb rating of movies by {actor} is {avg_rating:.1f}")

    def exit_menu(self):
        self.destroy()
        self.parent.deiconify()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
