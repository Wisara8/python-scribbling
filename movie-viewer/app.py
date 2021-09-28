import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Enter movie title: ")
    release_date = input("release date in dd-mm-yyyy: ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(header, movies):
    print(f"--- {header} movies ---")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("---  \n")


def print_watched_movie_list(username, movies):
    print(f"== {username}'s watched movies -- ")
    for movie in movies:
        print(f"{movie[1]}")
    print("---- \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie = input("Enter movie title: ")
    database.watch_movie(username, movie)


user_input = input(menu)

while user_input != "6":
    if user_input == "1":
        prompt_add_movie()
        break
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
        break
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
        break
    elif user_input == "4":
        prompt_watch_movie()
        break
    elif user_input == "5":
        username = input("Username: ")
        movies = database.get_watched_movies(username)
        print_watched_movie_list(username, movies)
        break
    else:
        print("Invalid input, please try again!")
