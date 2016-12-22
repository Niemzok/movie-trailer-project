import media
import fresh_tomatoes

#The block below stores the movies and series and related data.
toy_story = media.Movie("Toy Story",
                        "8/10",
                        "A story of a boy and his toys that come to life",
                        "http://1.bp.blogspot.com/-4CEJ24flM5U/T-ePLTwLdyI/AAAAAAAAHcQ/GGYVN8SVxG0/s1600/Toy+Story+%281995%29+1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "6/10",
                     "A marine on an alien planet",
                     "http://www.coolshite.net/wp-content/uploads/2009/12/Avatar-Poster.jpeg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


pulp_fiction = media.Movie("Pulp Fiction",
                           "10/10",
                           "A mad story about 2 gangsters and a surprising mission",
                           "http://www.cinemasterpieces.com/pulpfictionrecalledreal.jpg",
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")


school_of_rock = media.Movie("School of Rock",
                           "7/10",
                           "Storyline",
                           "http://images.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74")

godfather = media.Movie("The Godfather",
                        "10/10",
                        "Storyline",
                        "http://3.bp.blogspot.com/-kfFobXahgCI/T2e9e7R6uwI/AAAAAAAAAxY/tZtoOySAHKs/s1600/the-godfather-movie-poster-1020243893.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

emperors_new_groove = media.Movie("The Emperor's New Groove",
                        "9/10",
                        "Storyline",
                        "http://www.my-sf.com/wp-content/uploads/2015/09/The-Emperors-New-Groove-theatrical-teaser-poster-692x1024.jpg",
                        "https://www.youtube.com/watch?v=Hjvy8vc39kw")

once_upon_a_time = media.Movie("Once Upon a Time in America",
                        "7/10",
                        "Storyline",
                        "http://4.bp.blogspot.com/-uDbFoiRJ6UA/UCTSS-MrJ7I/AAAAAAAAE9I/XtappAzvt7Y/s400/once-upon-a-time-in-america-poster-3.jpg",
                        "https://www.youtube.com/watch?v=17dPdkKGMeo")

game_of_thrones = media.Series("Game of Thrones",
                               "10/10",
                               "http://blog.moviepostershop.com/wp-content/uploads/2011/03/Game-of-Thrones-poster.jpg",
                               "https://www.youtube.com/watch?v=BpJYNVhGf1s",
                               7,
                               73)

family_guy = media.Series("Family Guy",
                               "8/10",
                               "http://fanaru.com/family-guy/image/47609-family-guy-family-guy-poster.jpg",
                               "https://www.youtube.com/watch?v=g-jW547kTLo",
                               15,
                               281)

crown = media.Series("The Crown",
                     "8/10",
                     "http://assets.goodhousekeeping.co.uk/main/embedded/33995/the-crown-poster.jpg",
                     "https://www.youtube.com/watch?v=JWtnJjn6ng0",
                     1,
                     10)

mad_men = media.Series("Mad Men",
                     "9/10",
                     "http://celebritytravel.tv/wp-content/uploads/2014/04/mad_men_poster_by_supafly_01-d6pol34.jpg",
                     "https://www.youtube.com/watch?v=m7NChV93LBw",
                     7,
                     92)

movies = [toy_story, avatar, pulp_fiction, school_of_rock, godfather,
          emperors_new_groove, once_upon_a_time]

series = [game_of_thrones, family_guy, crown, mad_men]

fresh_tomatoes.open_movies_page(movies, series)
