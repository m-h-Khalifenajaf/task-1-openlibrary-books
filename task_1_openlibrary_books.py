import requests
import csv


forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

check = True
while check:
    topic = input("Enter a topic: ")
    check = False
    for char in forbidden_characters:
        if char in topic:
            print("Invalid character!")
            check = True
            break

params = {
    "q": topic,
    "limit": 50
}

url = "https://openlibrary.org/search.json"

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

except requests.exceptions.Timeout:
    print("The request timed out.")
    exit()

except requests.exceptions.ConnectionError:
    print("Failed to connect to the server.")
    exit()

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code}")
    exit()


data = response.json()
books = data["docs"]


filtered_books = []

for book in books:
    if book.get("first_publish_year", 0) > 2000:
        filtered_books.append(book)


fieldnames = [
    "title",
    "author_name",
    "first_publish_year",
    "language",
    "edition_count"
]

for book in filtered_books:
    for key in book.keys():
        if key not in fieldnames:
            fieldnames.append(key)


for book in filtered_books:
    for key in book:
        if isinstance(book[key], list):
            book[key] = "; ".join(map(str, book[key]))

filtered_books_sorted = sorted(filtered_books, key=lambda book: book["title", ""])

with open(f"Books about {topic}.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_books_sorted)


print("CSV file created successfully.")
print(f"Total books: {len(books)}")
print(f"Filtered books: {len(filtered_books_sorted)}")
