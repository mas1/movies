import media   # Contains Movie class
import fresh_tomatoes   # Contains html and stylesheet


# List movies below

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1"\
                        "/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/"\
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

walle = media.Movie("Wall-E",
                    "A robot love story for kids",
                    "http://img.subom.net/media/b_poster"\
                    "/20/910970_120.jpg",
                    "https://www.youtube.com/watch?v=ZisWjdjs-gM")

troy = media.Movie("Troy",
                   "Brad Pitt killing people",
                   "http://i.ebayimg.com/images/g/vmoAAO"\
                   "xyY3ZRntCX/s-l300.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY")

# Create an array containing movies
movies = [toy_story, avatar, walle, troy]
fresh_tomatoes.open_movies_page(movies)
