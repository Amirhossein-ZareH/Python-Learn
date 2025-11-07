#book

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percent):
        """E'lam takhfif bar rooye gheymat ketab"""
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount
        print(f"Price jadid ketab '{self.title}' ba takhfif {discount_percent}%: {self.price} toman")

    def info(self):
        """Namayesh moshakhasat kamel ketab"""
        print("\nMoshakhasat ketab:")
        print(f"Onvan ketab: {self.title}")
        print(f"Nevisande: {self.author}")
        print(f"Gheymat: {self.price} toman")


# Gereftan etelaat az user
title = input("Onvan ketab ra vared konid: ")
author = input("Name nevisande ra vared konid: ")

while True:
    try:
        price = float(input("Gheymat ketab (toman) ra vared konid: "))
        break
    except ValueError:
        print("Lotfan yek adad moteber vared konid.")

book = Book(title, author, price)
book.info()

# E'lam takhfif
while True:
    try:
        discount = float(input("Darsad takhfif ra vared konid: "))
        break
    except ValueError:
        print("Lotfan yek adad moteber vared konid.")

book.apply_discount(discount)
book.info()


#movie

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating 

    def describe(self):
        """Namayesh etelaat film"""
        print(f"\nMovie: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}/10")
        if self.rating > 8:
            print("In film yeki az behtarin-hast! 🎥🔥")

    def rate(self):
        """Gereftan emtiaz jadid az user va update kardan"""
        try:
            new_rating = float(input(f"Emtiaz jadid baraye '{self.title}' ra vared konid (0-10): "))
            if 0 <= new_rating <= 10:
                self.rating = new_rating
                print(f"Emtiaz film '{self.title}' be {self.rating} update shod.")
            else:
                print("Error: Emtiaz bayad beyn 0 ta 10 bashad!")
        except ValueError:
            print("Error: Lotfan yek adad sahih vared konid.")


# Namune estefade
movie1 = Movie("Inception", "Sci-Fi/Thriller", 9)
movie1.describe()

movie1.rate()
movie1.describe()


#point

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other_point):
        """Mohasebe fasele beyn do noghte"""
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

p1 = Point(3, 4)
p2 = Point(0, 0)

print(f"Fasele beyn p1 va p2: {p1.distance_from(p2)}")

