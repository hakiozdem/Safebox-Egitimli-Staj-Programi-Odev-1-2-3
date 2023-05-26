# -*- coding: utf-8 -*-
from movie import Movie
import re 
import time

class MovieSystem:
    storage = "movies.txt"
    movie_list = []
    
    def add_movie(self):
        movie_name = input("Enter Movie Name: ")
        movie_director = input("Enter Movie Director: ")
        movie_type = input("Enter Movie Type: ")
        
        file = open(self.storage,"a")
        file.write(movie_name.lower+","+movie_director.lower()+","+movie_type.lower()+"\n")
        file.close()
        self.__fill_or_refresh_list()
        return "Movie added successfully"
    
    def __fill_or_refresh_list(self):
        print("System in reload! Please wait")
        time.sleep(2)
        self.movie_list = []
        try:
            file = open(self.storage,"r")
            lines = file.readlines()
            file.close()
            for line in lines:
                a_line = line.replace("\n","").split(",")
                movie = Movie(a_line[0], a_line[1], a_line[2])
                self.movie_list.append(movie)
        except IOError:
            print("There is no movie, add some movie")
            self.add_movie()
            
        
    def search_movie(self): #Just for fun.
        if len(self.movie_list) != 0:
            options = "Search for title, director or type"
            print(options)
            pattern = input("Enter something: ")
            pattern_as_object = re.compile(r"\b{}\b".format(pattern.lower()))
            matches = [movie for movie in self.movie_list if pattern_as_object.search(movie.movie_name) or pattern_as_object.search(movie.movie_director) or pattern_as_object.search(movie.movie_type)]
            print("Here are yout movies:")
            for match in matches:
                print(match)
        else:
            print("Cache is empty, please wait to reload or add movie.")
            self.__fill_or_refresh_list()
    
    def remove_movie(self):
        if len(self.movie_list) != 0:
            temp_movie_list = []
            value = input("Please enter the movie name: ")
            with open(self.storage,"r") as file:
                for line in file:
                    if not line.startswith(value):
                        a_line = line.replace("\n","").split(",")
                        movie = Movie(a_line[0], a_line[1], a_line[2])
                        temp_movie_list.append(movie)
                        
            with open(self.storage,"w") as file:
                for movie in temp_movie_list:
                    file.write(movie.movie_name+","+movie.movie_director+","+movie.movie_type+"\n")
                
                self.__fill_or_refresh_list()
            
            return "Movie removed succesfully"
        
        else:
            print("Cache is empty, please wait to reload or add movie.")
            self.__fill_or_refresh_list()
    
    def list_movies(self):
        if len(self.movie_list) != 0:
            print("*******************")
            for i in range(len(self.movie_list)):
                print(str(i)+". Movie \n"+self.movie_list[i].__str__())
                print("*******************")
        else:
             print("Cache is empty, please wait to reload or add movie.")
             self.__fill_or_refresh_list()
if __name__=="__main__":
    system = MovieSystem()
    while True:
        print("System in reload!!")
        print("Welcome to Movie Management System\n")
        options = "1. Add a movie\n"+"2. Remove a movie\n"+"3. Search Bar\n"+"4. List all movies\n"+"5. Quit system\n"
        print(options)
        option = int(input("Please select an option: "))
        if option == 1:
            print(system.add_movie())
        elif option ==2:
            print(system.remove_movie())
        elif option == 3:
            system.search_movie()
        elif option == 4:
            system.list_movies()
        elif option == 5:
            print("Thank you for using!!!")
            break
        else:
            print("Please enter an valid option")

            
                
                
    
    
        
            
        
