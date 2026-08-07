class SocialMedia:

    CEO = "Mark"

    def like(self):
        print("Liked")

    def comment(self):
        print("Commented")

    def post(self):
            print("Posted")

facebook = SocialMedia()
facebook.comment()
facebook.post()
facebook.like()


# class car:

#     color = "Black"
#     brand = "Rolls Royce"
#     milage = "3mph"

#     def engin(self):
#         print("RR Engine")

#     def drive(self):
#         print("Driving")

#     def honk(self):
#         print("Peeeeeeeeeeeeeeeeee")

# a = car()
# b = car()

# print(a.brand)
# print(b.brand)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.brand)
# print(b.brand)

class Dog:

    species = "GS"

    def eat(self):
        self.b = 50
        print(f"hungry right now.")

    def bark(self):
        print(self.b)
        print(f"says woof!")

a = Dog()
a.eat()
a.bark()