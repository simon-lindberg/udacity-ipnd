import fresh_tomatoes
import media

# Create a new movie 'Toy Story'
toy_story = media.Movie(
    "Toy Story",
    "A story about a boy and his toys that comes to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc?t=10")

avatar = media.Movie(
    "Avatar",
    "A marrine on an alien planet",
    "http://www.impawards.com/2009/posters/avatar.jpg",
    "https://youtu.be/d1_JBMrrYw8?t=11"
    )

interstellar = media.Movie(
    "Interstellar",
    "On Earth, crop blight has caused civilization to regress...",
    "http://bit.ly/1DrGmUz",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Define array for all movies
movies = [toy_story, avatar, interstellar]

fresh_tomatoes.open_movies_page(movies)
