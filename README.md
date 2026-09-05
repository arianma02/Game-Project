# Steam Games Search & Recommendation

A small Python project for searching, filtering and recommending games from a Steam dataset.

Games can be filtered by name, genre, platform, price and rating. Recommendations are based on shared genres and Steam tags, with ratings used as an additional ranking factor.

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

Create the database:

```
python setup_database.py
```

Run the program:

```
python main.py
```

Run tests:

```
python -m pytest
```

Run the data analysis:

```
python analysis.py
```

## Tools

Python, SQL/SQLite, Pandas, pytest, Matplotlib

## Dataset

Steam Store Games dataset by Nik Davis.