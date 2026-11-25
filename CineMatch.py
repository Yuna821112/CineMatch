class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []
        self.watchlist = []
    def add_movie(self, title, genre, rating):
        movie = {'title': title, 'genre': genre, 'rating': rating}
        self.movies.append(movie)
        print(f"Movie '{title}' added successfully.")

    def search_movie(self, keyword):
        results = [movie for movie in self.movies if keyword.lower() in movie['title'].lower() or keyword.lower() in movie['genre'].lower()]
        if results:
            print(f"Search results for '{keyword}':")
            for movie in results:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
        else:
            print(f"No movies found for '{keyword}'.")

    def recommend_top_movies(self, N):
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        top_movies = sorted_movies[:N]
        print(f"Top {N} movies based on rating:")
        for movie in top_movies:
            print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
    
    def recommend_by_genre(self, genre):
        genre_movies = []

        for movie in self.movies:
            if movie['genre'].lower() == genre.lower():
                genre_movies.append(movie)

        if genre_movies:
            sorted_movies = sorted(
                genre_movies,
                key=lambda x: x['rating'],
                reverse=True
            )

            print(f"Top 3 movies in {genre}:")

            for movie in sorted_movies[:3]:
                print(f"Title: {movie['title']}, Rating: {movie['rating']}")
        else:
            print(f"No movies found in {genre}.")
    
    def delete_movie(self, title):
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                self.movies.remove(movie)
                print(f"Movie '{title}' deleted successfully.")
                return
        print(f"No movie found with title '{title}'.")
    def add_to_watchlist(self, title):
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                if movie in self.watchlist:
                    print("This movie is already in your watchlist.")
                else:
                    self.watchlist.append(movie)
                    print(f"'{movie['title']}' added to your watchlist.")
                return

        print("Movie not found.")
    def view_watchlist(self):
        if not self.watchlist:
            print("Your watchlist is empty.")
        else:
            print("My Personal Watchlist:")
            for movie in self.watchlist:
                print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")

    def remove_from_watchlist(self, title):
        for movie in self.watchlist:
            if movie['title'].lower() == title.lower():
                self.watchlist.remove(movie)
                print(f"'{movie['title']}' removed from your watchlist.")
                return

        print("Movie not found in your watchlist.")

# Example usage:
if __name__ == "__main__":

    system = MovieRecommendationSystem()
    system.add_movie("The Shawshank Redemption", "Drama", 9.3)
    system.add_movie("The Godfather", "Crime", 9.2)
    system.add_movie("The Dark Knight", "Action", 9.0)
    system.add_movie("Pulp Fiction", "Crime", 8.9)
    system.add_movie("The Lord of the Rings: The Return of the King", "Fantasy", 8.9)
    system.add_movie("Forrest Gump", "Drama", 8.8)
    system.add_movie("Inception", "Sci-Fi", 8.8)
    system.add_movie("Fight Club", "Drama", 8.8)
    system.add_movie("The Matrix", "Sci-Fi", 8.7)
    system.add_movie("Goodfellas", "Crime", 8.7)
    system.add_movie("The Lord of the Rings: The Fellowship of the Ring", "Fantasy", 8.8)
    system.add_movie("The Lord of the Rings: The Two Towers", "Fantasy", 8.7)
    system.add_movie("Star Wars: Episode V - The Empire Strikes Back", "Sci-Fi", 8.7)
    system.add_movie("Interstellar", "Sci-Fi", 8.6)
    system.add_movie("City of God", "Crime", 8.6)
    system.add_movie("Spirited Away", "Animation", 8.6)
    system.add_movie("Saving Private Ryan", "War", 8.6)
    system.add_movie("The Green Mile", "Drama", 8.6)
    system.add_movie("Gladiator", "Action", 8.5)
    system.add_movie("The Lion King", "Animation", 8.5)
    # Additional movies for genre-based recommendations
    system.add_movie("The Pursuit of Happyness", "Drama", 8.0)

    system.add_movie("John Wick", "Action", 7.4)
    system.add_movie("Top Gun: Maverick", "Action", 8.2)
    system.add_movie("Die Hard", "Action", 8.2)

    system.add_movie("The Departed", "Crime", 8.5)

    system.add_movie("Harry Potter and the Sorcerer's Stone", "Fantasy", 7.6)
    system.add_movie("The Hobbit", "Fantasy", 7.8)

    system.add_movie("Arrival", "Sci-Fi", 7.9)

    system.add_movie("Coco", "Animation", 8.4)
    system.add_movie("Inside Out", "Animation", 8.1)
    system.add_movie("Finding Nemo", "Animation", 8.2)

    system.add_movie("1917", "War", 8.2)
    system.add_movie("Dunkirk", "War", 7.8)
    system.add_movie("Hacksaw Ridge", "War", 8.1)
    system.add_movie("Fury", "War", 7.6)

    system.add_movie("The Shining", "Horror", 8.4)
    system.add_movie("The Conjuring", "Horror", 7.5)
    system.add_movie("Insidious", "Horror", 6.8)
    system.add_movie("Get Out", "Horror", 7.8)
    system.add_movie("A Quiet Place", "Horror", 7.5)

    system.add_movie("The Hangover", "Comedy", 7.7)
    system.add_movie("Home Alone", "Comedy", 7.7)
    system.add_movie("Mean Girls", "Comedy", 7.1)
    system.add_movie("Mrs. Doubtfire", "Comedy", 7.1)
    system.add_movie("The Intern", "Comedy", 7.1)

    system.add_movie("Titanic", "Romance", 7.9)
    system.add_movie("The Notebook", "Romance", 7.8)
    system.add_movie("Pride and Prejudice", "Romance", 7.8)
    system.add_movie("La La Land", "Romance", 8.0)
    system.add_movie("Notting Hill", "Romance", 7.2)
    while True:
        print("\nMovie Recommendation System")
        print("1. Add a new movie")
        print("2. Search for movies by title or genre")
        print("3. Recommend top N movies based on rating")
        print("4. Delete a movie")
        print("5. Recommend top 3 movies by genre")
        print("6. Add a movie to my watchlist")
        print("7. View my watchlist")
        print("8. Remove a movie from my watchlist")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating (0-10): "))
            system.add_movie(title, genre, rating)
        elif choice == "2":
            keyword = input("Enter keyword to search (title or genre): ")
            system.search_movie(keyword)
        elif choice == "3":
            N = int(input("Enter number of top movies to recommend: "))
            system.recommend_top_movies(N)
        elif choice == "4":
            title = input("Enter the title of the movie to delete: ")
            system.delete_movie(title)
        elif choice == "5":
            genre = input("Enter your preferred genre: ")
            system.recommend_by_genre(genre)
        elif choice == "6":
            title = input("Enter movie title: ")
            system.add_to_watchlist(title)
        elif choice == "7":
            system.view_watchlist()
        elif choice == "8":
            title = input("Enter movie title to remove: ")
            system.remove_from_watchlist(title)
        elif choice == "9":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        
