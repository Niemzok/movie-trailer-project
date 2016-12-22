import webbrowser

class Video():
    """This class provides a general way to store Video related information.
        It is the Parent class to following Video type classes."""
    def __init__(self, title, rating, poster_image, trailer_youtube):
        self.title = title
        self.rating = rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)


class Movie(Video):
    """This class provides a way to store movie related information."""

    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_rating, movie_storyline, poster_image,
                  trailer_youtube):
        Video.__init__(self, movie_title, movie_rating, poster_image,
                        trailer_youtube)
        self.storyline = movie_storyline

class Series(Video):
    """This class provides a way to store Series related information."""

    def __init__(self, series_title, series_rating, poster_image,
                 trailer_youtube, number_of_seasons, number_of_episodes):
        Video.__init__(self,series_title, series_rating, poster_image,
                       trailer_youtube)
        self.number_of_seasons = number_of_seasons
        self.number_of_episodes = number_of_episodes
