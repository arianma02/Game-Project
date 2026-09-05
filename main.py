from database import (
    search_by_name,
    search_by_genre,
    search_by_max_price,
    search_by_min_rating,
    search_by_platform
)

from recommendations import recommend_games

print("Game Explorer")
print("1. Search by name")
print("2. Search by genre")
print("3. Maximum price")
print("4. Minimum rating")
print("5. Platform")
print("6. Recommend similar games")


choice = input("Choose: ")

if choice == "1":
    name = input("Game name: ")
    results = search_by_name(name)

elif choice == "2":
    genre = input("Genre: ")
    results = search_by_genre(genre)

elif choice == "3":
    price = float(input("Maximum price: "))
    results = search_by_max_price(price)

elif choice == "4":
    rating = float(input("Minimum rating (%): "))
    results = search_by_min_rating(rating)

elif choice == "5":
    platform = input("Platform: ")
    results = search_by_platform(platform)

elif choice == "6":
    game_name = input("Enter a game you like: ")

    results = recommend_games(game_name)

    if not results:
        print("Game not found.")
    else:
        for score, name, genres, rating, price in results:
            print(
                f"{name} | Rating: {rating:.1f}% | "
                f"Price: £{price:.2f}"
            )

else:
    results = []
    print("Invalid choice.")

for game in results:
    print(game)
