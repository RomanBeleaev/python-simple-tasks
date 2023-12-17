class Book:
    def __init__(self, title, pages, rating):
        self.title = title
        self.pages = pages
        self.rating = rating

    def __gt__(self, other):
        return self.rating > other.rating
    
    def info(self):
        print("##########Book##########")
        print(self.title, self. pages, self.rating)
        print("########################\n")

coolBook   = Book("First Book", 150, 4.0)
boringBook = Book("Second Book", 300, 2.0)

coolBook.info()
boringBook.info()

if coolBook > boringBook:
    print("First is better")