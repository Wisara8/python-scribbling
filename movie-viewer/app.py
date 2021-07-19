import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"
goodbye = "Exiting App, Goodbye"


print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Enter movie title: ")
    release_date = input("release date in dd-mm-yyyy: ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(movies):
    print("--- Upcoming movies ---")
    for movie in movies:
        print(f"{movie[0]} (on {movie[1]})")
    print("---  \n")


user_input = input(menu)

while user_input != "6":
    if user_input == "1":
        prompt_add_movie()
        break
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list(movies)
        break
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again!")
