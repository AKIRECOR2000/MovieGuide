#Akire Cormier, CIS261, Movie Guide Part2

with open("movies.txt", "w") as file:
        file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail\n")

def Movie_Guide():
    print("Movie List Program")
    print()
    print("Please select an option:")
    print("list: List all movies")
    print("add: Add a movie")
    print("delete: Delete a movie")
    print("exit: Exit Guide")
    
def list(file_name):
    movie_list = []
    with open(file_name, "r") as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list
        
def display_title(movie_list):
    print("\nMovies: ")
    for i, title in enumerate(movie_list, start = 1):
        print(f"{i}, {title}")
        
def add(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, "a") as file:
        file.write(title + "\n")
    print(f"\n'{title}' has been added.")
    
def delete(movie_list, i, file_name):
    if 1 <= i <= len(movie_list):
        delete = movie_list.pop(i -1)
        with open (file_name, "w") as file:
            file.write("\n".join(movie_list))
        print(f"\n'{delete}' has been deleted.")
    else:
        print("\nInvalid movie number, try again.")
        
def main():
    movie_file = "movies.txt"
    movie_list = list(movie_file)
    
    while True:
        Movie_Guide()
        option = input("Enter your option: ")
        if option == "list":
            display_title(movie_list)
        elif option == "add":
            new_title = input("Enter new movie title: ")
            add(movie_list, new_title, movie_file)
            display_title(movie_list)
        elif option == "delete":
            display_title(movie_list)
            i = int(input("Enter the movie number: "))
            delete(movie_list, i, movie_file)
            display_title(movie_list)
        elif option == "exit":
            print("See ya!")
            break
        else:
            print("Invalid option, try again.")
            
if __name__ == "__main__":
    main()
    