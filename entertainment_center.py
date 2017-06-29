import fresh_tomatoes
import media

#media is name of media file
#Movie is name of class defined in that file
toy_story = media.Movie("Toy Story", "A story of some toys", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar", "A story of an alien", 
						"http://highwaytomars.com/wp-content/uploads/2016/08/Avatar.jpeg", 
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")


movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)