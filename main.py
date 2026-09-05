from database import (
    search_by_name,
    search_by_genre,
    search_by_max_price,
    search_by_min_rating,
    search_by_platform
)

from recommendations import recommend_games


def print_games(results, info_label="Genres"):
    for name, info, rating, price in results:
        print(f"\n{name}")
        print(f"{info_label}: {info}")
        print(f"Rating: {rating:.1f}%")
        print(f"Price: £{price:.2f}")


while True:
    print("\nGame Explorer")
    print("1. Search by name")
    print("2. Search by genre")
    print("3. Maximum price")
    print("4. Minimum rating")
    print("5. Platform")
    print("6. Recommend similar games")
    print("7. Exit")

    choice = input("Choose: ").strip()

    # 1. SEARCH BY NAME
    if choice == "1":
        name = input("Game name: ").strip()

        if not name:
            print("Please enter a game name.")
            continue

        results = search_by_name(name)

        if not results:
            print("No games found.")
            continue

        print_games(results)


    # 2. SEARCH BY GENRE
    elif choice == "2":
        genre = input("Genre: ").strip()

        if not genre:
            print("Please enter a genre.")
            continue

        results = search_by_genre(genre)

        if not results:
            print("No games found for that genre.")
            continue

        print_games(results)


    # 3. MAXIMUM PRICE
    elif choice == "3":
        try:
            price = float(input("Maximum price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        results = search_by_max_price(price)

        if not results:
            print("No games found within that price.")
            continue

        print_games(results)


    # 4. MINIMUM RATING
    elif choice == "4":
        try:
            rating = float(input("Minimum rating (%): "))

            if rating < 0 or rating > 100:
                print("Rating must be between 0 and 100.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        results = search_by_min_rating(rating)

        if not results:
            print("No games found with that minimum rating.")
            continue

        print_games(results)


    # 5. PLATFORM
    elif choice == "5":
        platform = input("Platform: ").strip()

        if not platform:
            print("Please enter a platform.")
            continue

        results = search_by_platform(platform)

        if not results:
            print("No games found for that platform.")
            continue

        print_games(results, info_label="Platforms")


    # 6. RECOMMENDATIONS
    elif choice == "6":
        game_name = input("Enter a game you like: ").strip()

        if not game_name:
            print("Please enter a game name.")
            continue

        results = recommend_games(game_name)

        if not results:
            print("Game not found.")
            continue

        print("\nRecommendations:")

        for score, name, rating, price in results:
            print(f"\n{name}")
            print(f"Rating: {rating:.1f}%")
            print(f"Price: £{price:.2f}")


    # 7. EXIT
    elif choice == "7":
        print("Goodbye.")
        break


    # ANYTHING OTHER THAN 1–7
    else:
        print("Invalid choice. Choose a number from 1 to 7.")