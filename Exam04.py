class dog:
    def __init__(self, breed, color, height, weight):
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight

    def growth(self):
        self.height = self.height + (self.height / 100 * 10)
        self.weight = self.weight + (self.weight / 100 * 10)


dog_A = dog("Jack russell Terrier", "White", 30,7)
dog_A.growth()
print(dog_A.height)
print(dog_A.weight)
