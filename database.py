import sqlite3

def get_connection():
    return sqlite3.connect("games.db")


def search_by_name(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, genres, rating_percent, price
        FROM games
        WHERE name LIKE ?
        ORDER BY rating_percent DESC
        LIMIT 20
        """,
        (f"%{name}%",)
    )

    results = cursor.fetchall()
    connection.close()
    
    return results

def search_by_genre(genre):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, genres, rating_percent, price
        FROM games
        WHERE genres LIKE ?
        ORDER BY rating_percent DESC
        LIMIT 20
        """,
        (f"%{genre}%",)
    )

    results = cursor.fetchall()
    connection.close()

    return results

def search_by_max_price(price):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, genres, rating_percent, price
        FROM games
        WHERE price <= ?
        ORDER BY rating_percent DESC
        LIMIT 20
        """,
        (price,)
    )

    results = cursor.fetchall()
    connection.close()

    return results