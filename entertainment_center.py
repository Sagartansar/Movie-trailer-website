import fresh_tomatoes
import media



lucy = media.Movie("Lucy",
                    "Lucy is the story of a girl who take highly composit drugs accedintly and after that her brain get works 100%",
                    "https://en.wikipedia.org/wiki/Lucy_(2014_film)#/media/File:Lucy_(2014_film)_poster.jpg",
                    "https://www.youtube.com/watch?v=RnKVv8Lp_xU")

anonymous = media.Movie("anonymous",
                    "a movie on hackers life",
                    "https://en.wikipedia.org/wiki/Anonymous_(film)#/media/File:Anonymous_2011_film_poster.jpg",
                    "https://www.youtube.com/watch?v=4s5RmZ4l0PM")

doctor_strange = media.Movie("doctor_strange",
                    "a person got powers",
                    "https://en.wikipedia.org/wiki/Doctor_Strange#/media/File:Doctor_Strange_Vol_4_2_Ross_Variant_Textless.jpg",
                    "https://www.youtube.com/watch?v=HSzx-zryEgM")

Bahubali_2 = media.Movie("Bahubali-2",
                    "bahubali part 2 is a story of a king who killed by his love ones and revenge",
                    "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                    "https://www.youtube.com/watch?v=G62HrubdD6o")

hindi_medium = media.Movie("hindi_medium",
                    "this moive is a story of comdition indian education system",
                    "https://en.wikipedia.org/wiki/Hindi_Medium_(film)#/media/File:Hindi_Medium_Poster.jpg",
                    "https://www.youtube.com/watch?v=GjkFr48jk68")

dangal = media.Movie("dangal",
                    "dangal is a story of two sisters who fote for her dreams to become worlds greatest wrestlers.",
                    "https://en.wikipedia.org/wiki/File:Dangal_Poster.jpg",
                    "https://www.youtube.com/watch?v=x_7YlGv9u1g")


mindgamers = media.Movie("mindgamers",
                    "story about controling human mind",
                    "https://en.wikipedia.org/wiki/File:MindGamers_(2017_film)_poster.jpg",
                    "https://www.youtube.com/watch?v=Gb62EQyJFyo&t=21s")

transformers_5 = media.Movie("transformers_5",
                    "alines robots war",
                    "https://en.wikipedia.org/wiki/Transformers:_The_Last_Knight#/media/File:Transformers_The_Last_Knight_poster.jpg",
                    "https://www.youtube.com/watch?v=sgnO5fO46pE")

movies = [lucy, anonymous, doctor_strange, Bahubali_2, hindi_medium, dangal, mindgamers, transformers_5]
fresh_tomatoes.open_movies_page(movies)


