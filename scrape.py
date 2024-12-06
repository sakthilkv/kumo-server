from imdb import Cinemagoer


# Initialize the CinemaGoer instance
cm = Cinemagoer()

# List of movie titles
movies = [
    'The Grand Budapest Hotel',
    'Guardians of the Galaxy',
    'Into the Spider-Verse',
    'The Secret Life of Pets',
    'Life of Pi',
    'Coco',
    'Mad Max: Fury Road',
    'The Lion King',
    'Aladdin (2019)',
    'Doctor Strange',
    'The Lego Movie',
    'Thor: Ragnarok'
]
# Fetch poster URLs for each movie
for movie in movies:
    search_result = cm.search_movie(movie)
    if search_result:
        # Get the first movie from the search result
        movie_id = search_result[0].get_fullsizeURL()
        print(movie_id)
    else:
        print(f"No results found for {movie}")
