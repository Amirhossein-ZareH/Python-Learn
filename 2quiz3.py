class LibraryItem:
    def __init__(self, title, publisher, year):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.available = True

    def info(self):
        return f"Title: {self.title}, Publisher: {self.publisher}, Year: {self.year}, Available: {self.available}"

    def checkout(self):
        if self.available:
            self.available = False
            print(f"'{self.title}'hamin alan check out shod.")
        else:
            print(f"Motasefane, '{self.title}' alan dastres nist.")

    def return_item(self):
        self.available = True
        print(f"'{self.title}' barmigarde be library.")

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if isinstance(other, LibraryItem):
            return self.year == other.year
        return False


class Book(LibraryItem):
    def __init__(self, title, publisher, year, author, pages):
        super().__init__(title, publisher, year)
        self.author = author
        self.pages = pages

    def info(self):
        return (f"Ketab: {self.title}\n"
                f"Nevisande: {self.author}\n"
                f"Entesharat: {self.publisher}\n"
                f"Sale enteghal: {self.year}\n"
                f"Tedad safahat: {self.pages}\n"
                f"Dastres: {self.available}")

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.year == other.year
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented


class Magazine(LibraryItem):
    def __init__(self, title, publisher, year, month, pages):
        super().__init__(title, publisher, year)
        self.month = month
        self.pages = pages

    def info(self):
        return (f"Majale: {self.title}\n"
                f"Entesharat: {self.publisher}\n"
                f"Sale enteghal: {self.year}\n"
                f"Mah: {self.month}\n"
                f"Tedad safahat: {self.pages}\n"
                f"Dastres: {self.available}")

    def __str__(self):
        return f"'{self.title}' ({self.month} {self.year})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Magazine):
            return self.year == other.year
        return False

    def __lt__(self, other):
        if isinstance(other, Magazine):
            return self.pages < other.pages
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Magazine):
            return self.pages > other.pages
        return NotImplemented


# Test
book1 = Book("dezire", "bargiran", 2014, "anne marie silenko", 350)
book2 = Book("myazaki", "japanese books", 1999, "hiao myazaki", 420)

mag1 = Magazine("batman", "dc", 2023, "November", 50)
mag2 = Magazine("dota2", "valve", 2022, "October", 40)

print(book1)
print(len(book1))
print(book1 == book2)
print(book1 > book2)

print("\n" + str(mag1))
print(len(mag1))
print(mag1 == mag2)
print(mag1 < mag2)

book1.checkout()
book1.checkout()
book1.return_item()
