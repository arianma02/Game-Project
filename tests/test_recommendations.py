from recommendations import split_values, recommend_games

def test_split_values():
    result = split_values("Action;RPG;Adventure")
    assert result == {"action", "rpg", "adventure"}

def test_split_values_empty():
    result = split_values("")
    assert result == set()


def test_split_values_spaces_and_case():
    result = split_values(" Action ; RPG ; Adventure ")
    assert result == {"action", "rpg", "adventure"}


def test_recommendation_limit():
    results = recommend_games("Portal 2", limit=3)
    assert len(results) <= 3


def test_unknown_game():
    results = recommend_games("THIS_GAME_DOES_NOT_EXIST_12345")
    assert results == []