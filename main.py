from database import search_by_name, search_by_genre, search_by_max_price

print("Game Explorer")
print("1. Search by name")
print("2. Search by genre")
print("3. Maximum price")

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

else:
    results = []
    print("Invalid choice.")

for game in results:
    print(game)
