import webbrowser

"""
This module contain the Movie class which will
be used from the entertainment_center.py.
"""

# Instantiate the Movie() class


class Movie():
    """
    Movie object initialized below.

    """
    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
