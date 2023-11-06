#Akire Cormier, CIS261, Movie Guide Part1 
def Movie_Guide():
    print("Welcome to my Movie Guide!")
    print()
    print("Please select an option:")
    print("list: List all movies")
    print("add: Add a movie")
    print("delete: Delete a movie")
    print("exit: Exit Guide")
    
def list(movies):
    print("Here are the movies:")
    for index, movie in enumerate(movies):
        print(f"{index+1}. {movie}")
        print()
        

def add(movies):
    movie = input("Name:")
    movies.append(movie)
    print("New movie title added successfully!")
    

def delete(movies):
    number = int(input("Number: "))
    if number < 1 or number > len(movies):
        print("Movie not found. \n")
    else:
        movie = movies.pop(number - 1)
        print(f"{movie} was deleted. \n")
        
def main():
    movies = ["Insidious", "The Conjuring", "Hereditary"]
    
    Movie_Guide()
    
    while True:
        command = input("Option:  ")
        if command.lower() == "list":
            list(movies)
        elif command.lower() == "add":
            add(movies)
        elif command.lower() == "del":
            delete(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Command invalid, please try again. \n")
    print("See ya!")
        
if __name__ == "__main__":
    main()
         

    
   
    