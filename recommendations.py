from database import get_connection

def split_values(text):
    if not text:
        return set()

    return {value.strip().lower() for value in text.split(";")}


def recommend_games(game_name, limit=5):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, genres, steamspy_tags
        FROM games
        WHERE name LIKE ?
        LIMIT 1
        """,
        (f"%{game_name}%",)
    )

    target = cursor.fetchone()

    if target is None:
        connection.close()
        return []

    target_name, target_genres, target_tags = target

    target_genres = split_values(target_genres)
    target_tags = split_values(target_tags)

    cursor.execute(
        """
        SELECT name, genres, steamspy_tags, rating_percent, price
        FROM games
        WHERE name != ?
        AND rating_percent IS NOT NULL
        """,
        (target_name,)
    )

    candidates = cursor.fetchall()
    connection.close()

    recommendations = []

    for name, genres, tags, rating, price in candidates:
        genres = split_values(genres)
        tags = split_values(tags)

        shared_genres = len(target_genres & genres)
        shared_tags = len(target_tags & tags)

        score = (
            shared_genres * 3
            + shared_tags * 2
            + rating / 100
        )

        if shared_genres > 0 or shared_tags > 0:
            recommendations.append(
                (score, name, genres, rating, price)
            )

    recommendations.sort(reverse=True)

    return recommendations[:limit]