# -*- coding: utf-8 -*-
class Movie:
    def __init__(self,movie_name,movie_director,movie_type):
        self.movie_name = movie_name
        self.movie_director = movie_director
        self.movie_type = movie_type
     
    def __str__(self):
        return "Movie Name: "+self.movie_name.capitalize()+"\n"+"Movie Director: "+self.movie_director.capitalize()+"\n"+"Movie Type: "+self.movie_type.capitalize()
    
    
        
