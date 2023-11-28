# Advanced dataset for manipulation
library = [
    {'title': 'A Fictional Tale', 'author': 'Phil Fiction', 'genres': {'Fiction', 'Mystery'}},
    {'title': 'The Sci-Fi Special', 'author': 'Simon Sci', 'genres': {'Science Fiction', 'Adventure'}},
    {'title': 'The Story of Fiction', 'author': 'Francis Ficto', 'genres': {'Fiction', 'Romance'}},
    {'title': 'A True Story', 'author': 'John Truth', 'genres': {'Non-Fiction', 'History'}}
]

# Creating set for all genres
all_genres = set()
for book in library:
    all_genres.update(book['genres'])
print("Set of all unique genres:", all_genres)

fiction_books = [book['title'] for book in library if 'Fiction' in book['genres']]
print("\nFiction books:", fiction_books)

# Creating frozenset for immutable genres
immutable_genres = frozenset(library[0]['genres'])
print(f"\nImmutable genres for {library[0]['title']}:", immutable_genres)

# Creating nested data structure
books_by_genre = {}
for book in library:
    for genre in book['genres']:
        if genre not in books_by_genre:
            books_by_genre[genre] = []
        books_by_genre[genre].append(book['title'])

print("Books grouped by genre:")
for genre, books in books_by_genre.items():
    print(f"\n{genre}: {', '.join(books)}")