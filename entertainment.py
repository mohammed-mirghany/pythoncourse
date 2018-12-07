import media
import fresh_tomatoes
avatar = media.Movie("Avatar","a marine on bita3 bita3", "http://www.impawards.com/2009/posters/avatar.jpg" ,"https://www.youtube.com/watch?v=yiD-8SxaON4")
hisham = media.Movie("mohamed","wd hisham ya5", "https://images.performgroup.com/di/library/GOAL/ef/1e/mauro-icardi-inter_1a2bzcgydljuj197iggcnzgct5.jpg?t=1814868439" ,"https://www.youtube.com/watch?v=fK5LYVd1MHs")
movies = [avatar,hisham]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)