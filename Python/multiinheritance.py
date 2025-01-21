class organism:
    pavi="true"
class animal(organism):
    def bark(self):
        print("I am writing coding now")
class mouse(animal):
    def bar(self):
        print("I am learning now in my laptop")
bob=mouse()
print(bob.pavi)
bob.bark()
bob.bar()
