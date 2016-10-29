import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 
						'a story of a boy',
						' http://upload.wikimedia.org/wikipedia/en/1/13/Toy_story.jpg',
						'https://www.youtube.com/watch?v=vwyZH85NQC4' )

avatar = media.Movie('Avatar', 
					'Marinac na stranom planetu',
					'https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg',
					'https://www.youtube.com/watch?v=aVdO-cx-McA')

braveheart = media.Movie('Braweheart', 
					'Strange new world...',
					'https://en.wikipedia.org/wiki/Braveheart#/media/File:Braveheart_imp.jpg',
					'https://www.youtube.com/watch?v=j53_WxqPZ7c')

school_of_rock = media.Movie('School of Rock', 
					'Škola rokenrolla',
					'https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg',
					'https://www.youtube.com/watch?v=oP7kExN8LFA')

monsters_university = media.Movie('Monsters University', 
					'Monsters University...stroyline',
					'https://en.wikipedia.org/wiki/Monsters_University#/media/File:Monsters_University_poster_3.jpg',
					'https://www.youtube.com/watch?v=xBzPioph8CI')

print(media.Movie.__doc__)
print(media.Movie.__dict__)	
print(media.Movie.__name__)	
print(media.Movie.__module__)	
# print(media.Movie.VALID_RATINGS)
# movies = [toy_story, avatar, braveheart, school_of_rock, monsters_university]
# fresh_tomatoes.open_movies_page(movies)
# print(monsters_university.title)
# print(monsters_university.storyline)
# monsters_university.show_image()
# monsters_university.show_trailer()