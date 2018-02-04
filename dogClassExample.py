class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def walk(self):
        print("{} the dog walks".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))


def main():
    spot = Dog("Spot", 25, 57)

    spot.run()
    spot.walk()


main()

