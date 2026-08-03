from movie_api import get_movie

print("\nMovie Search App")
print("*" * 30)
def search_movie():
    movie = input("Enter the name of Movie: ")
    data = get_movie(movie)

    if data:
        title = data["Title"]
        year = data["Year"]
        genre = data["Genre"]
        director = data["Director"]
        actors = data["Actors"]
        runtime = data["Runtime"]
        rating = data["imdbRating"]
        plot = data["Plot"]
        language = data["Language"]
        country = data["Country"]

        print("\n==============================")
        print("🎬 Movie Information")
        print("==============================")

        print(f"Title       : {title}")
        print(f"Year        : {year}")
        print(f"Genre       : {genre}")
        print(f"Director    : {director}")
        print(f"Actors      : {actors}")
        print(f"Runtime     : {runtime}")
        print(f"IMDb Rating : {rating}")
        print(f"Language    : {language}")
        print(f"Country     : {country}")

        print("\nPlot:")
        print(plot)
    else:
        print("\nMovie not found!. ")

search_movie()