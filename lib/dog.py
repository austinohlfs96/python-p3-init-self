# !/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
       self.name = name
       self.breed = breed

    # def bark(self):
    #     print("Woof!")

    # def showing_self(self):
    #     return self

# fido = Dog("Fido")
# # Fido is born!
# fido.showing_self()
# # <__main__.Dog object at 0x104f8bfa0>

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog ("Rex")

print(f"{dog1.name} is a {dog1.breed}")
print(f"{dog2.name} is a {dog2.breed}")
