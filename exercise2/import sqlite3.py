import sqlite3

# Read the file and copy the content to list
with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

# Establish connection with SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                  (movieID TEXT, movieName TEXT, movieYear INTEGER, imdbRating REAL)''')

# Insert data into the table
for line in stephen_king_adaptations_list:
    values = line.strip().split(",")
    cursor.execute('INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)',
                   (values[0], values[1], int(values[2]), float(values[3])))

# Save changes and close connection
conn.commit()
conn.close()

# Function to search for movies in the database based on user input
def search_movies():
    while True:
        print("\nSearch options:")
        print("1. Movie name")
        print("2. Movie year")
        print("3. Movie rating")
        print("4. STOP")

        option = input("Enter your choice: ")

        if option == "1":
            movie_name = input("Enter the name of the movie: ")
            # Establish connection with SQLite database
            conn = sqlite3.connect("stephen_king_adaptations.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
            result = cursor.fetchall()

            if len(result) > 0:
                print("Movie details:")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No such movie exists in our database")

            # Close connection
            conn.close()

        elif option == "2":
            movie_year = input("Enter the year: ")
            # Establish connection with SQLite database
            conn = sqlite3.connect("stephen_king_adaptations.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (int(movie_year),))
            result = cursor.fetchall()

            if len(result) > 0:
                print("Movie(s) released in", movie_year, ":")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies were found for that year in our database")

            # Close connection
            conn.close()

        elif option == "3":
            movie_rating = input("Enter the minimum IMDB rating: ")
            # Establish connection with SQLite database
            conn = sqlite3.connect("stephen_king_adaptations.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (float(movie_rating),))
            result = cursor.fetchall()

            if len(result) > 0:
                print("Movie(s) with rating", movie_rating, "and above:")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies at or above that rating were found in the database.")

            # Close connection
            conn.close()

        elif option == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")

# Call the search_movies function to start the search loop
search_movies()