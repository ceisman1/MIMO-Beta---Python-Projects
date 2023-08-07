hamlet_info = ("William Shakespeare", "Tragedy", 1603)
martian_chronicles_info =  ("Ray Bradbury", "Science fiction", 1950)

my_books = {
	"Hamlet": hamlet_info,
	"The Martian Chronicles": martian_chronicles_info
}
print(f"My books: {my_books}")

my_books["Fahrenheit 451"] = ("Ray Bradbury", "Dystopian", 1953)
print(f"Fahrenheit 451 info: {my_books['Fahrenheit 451']}")

my_books_authors = set()

for book in my_books:
	book_info = my_books[book]
	author = book_info[0]
	my_books_authors.add(author)
print(f"Authors: {my_books_authors}")

is_my_author = "Ray Bradbury" in my_books_authors
if is_my_author:
	print("Ray Bradbury belongs to my authors!")
