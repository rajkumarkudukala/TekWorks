def add(books, key, value):
    books[key] = value

def remove(books,key):
    if key in books:
        books.pop(key)
    
def search(books,key):
    if key in books:
        print(books[key])

def display(books):
    print(books)

def count(books):
    print(len(books))

def lookup(books, value):
    for i in books:
        if books[i] == value:
            print(i,value)
            break



books = {}
add(books, 100, "got")
add(books, 101, "dune")
add(books,103,"spider-man")
add(books,104,"winds of winter")
add(books,104,"ACD")

display(books)

remove(books,104)

count(books)

lookup(books,"spider-man")