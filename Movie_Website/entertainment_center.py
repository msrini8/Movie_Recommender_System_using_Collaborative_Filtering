import fresh_tomatoes
import media

school_of_rock = media.Movie("School of Rock","A guy who gets kicked out of his rock band, tries to form a school rock band and competes in a rock competition",
                             "https://www.google.com/search?q=school+of+rock&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi07NHwt-jZAhXLmVkKHeT0BDMQ_AUIDCgD&biw=1440&bih=826#imgrc=NpymP4sprY23BM:",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

english_vinglish = media.Movie("English Vinglish","A small town housewife tries to learn English ater being mocked by her family",
                               "https://en.wikipedia.org/wiki/English_Vinglish#/media/File:English_Vinglish_poster.jpg",
                               "https://www.youtube.com/watch?v=wmGVY4T88dc")

masaan = media.Movie("Masaan","In the holy city on the banks of the Ganges, where cruel punishment for those who do not respect moral traditions are given, Deepak, a young man from a poor neighborhood, falls hopelessly in love with a young girl from a different caste.",
                    "https://en.wikipedia.org/wiki/Masaan#/media/File:Masaan_poster.jpg",
                    "https://www.youtube.com/watch?v=IVZzYa0MxM8")

three_idiots = media.Movie("3 Idoits","A bet gives two college friends a chance to look for their long-lost friend whose existence seems rather elusive.",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                      "https://www.youtube.com/watch?v=xvszmNXdM4w")

bajirao_mastani = media.Movie("Bajirao Mastani","The heroic Peshwa Bajirao, married to Kashibai, falls in love with Mastani, a warrior princess in distress",
                              "https://upload.wikimedia.org/wikipedia/en/c/c0/Bajirao_Mastani_poster.jpg",
                              "https://www.youtube.com/watch?v=eHOc-4D7MjY")

dhoom2 = media.Movie("Dhoom 2","Three Indian police officers in Mumbai, join forces to bring down a cunning criminal.",
                     "https://en.wikipedia.org/wiki/Dhoom_2#/media/File:D2-poster-ver2.jpg",
                     "https://www.youtube.com/watch?v=sWE458JxSZA")

googly = media.Movie("Googly","A college friendship turns into a mutual attraction, but a small misunderstanding causes them to part ways.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3e/Googly_2013_Kannada_Film.jpg",
                     "https://www.youtube.com/watch?v=QhhbBpzR2eA")

dangal = media.Movie("Dangal","After his failure at winning a gold medal for the country, Mahavir Phogat vows to realize his dreams by training his daughters for the Commonwealth Games despite societal pressures.",
                     "https://en.wikipedia.org/wiki/Dangal_(film)#/media/File:Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

lucia = media.Movie("Lucia","An insomniac tries a new drug known as Lucia, which causes his dreams to spill over into reality.",
                    "https://en.wikipedia.org/wiki/Lucia_(2013_film)#/media/File:Lucia_kannada_film_poster1.jpg",
                    "https://www.youtube.com/watch?v=pgIL2H-OdcA")

kirik_party = media.Movie("Kirik Party","Kirik Party is the story of a gang of mischievous students, lead by the protagonist Karna, who has just joined an engineering college.",
                          "https://en.wikipedia.org/wiki/Kirik_Party#/media/File:Kirik_Part_Poster.jpg",
                          "https://www.youtube.com/watch?v=IfvnbER_6sQ")

movies = [school_of_rock, english_vinglish, masaan, three_idiots, bajirao_mastani, dhoom2, googly, dangal, lucia, kirik_party]
fresh_tomatoes.open_movies_page(movies)