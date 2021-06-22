import random


class Dog:
    firstNames = ["Spot", "Fluffy", "Cerberus", "Mouse"]
    lastNames = ["Catcher", "Sparrow", "Mountain", "Hunter", "Canis", "Câine"]
    breeds = ["German Shepherd", "Siberian Husky", "Great Dane"]
    colors = ["Black", "Brown", "Golden", "Grey"]
    conditions = ["Hungry", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]

    def __init__(self,
                 _Instance_firstName="",
                 _Instance_lastName="", _Instance_weight=0,
                 _Instance_breed="",
                 _Instance_age=0,
                 _Instance_color="",
                 _Instance_condition=""):
        self._Instance_firstName = [_Instance_firstName or self.getRandValue(self.firstNames), "First Name"]
        self._Instance_lastName = [_Instance_lastName or self.getRandValue(self.lastNames), "Last Name"]
        self._Instance_weight = [int(_Instance_weight) or random.randint(1, 100), "Weight"]
        self._Instance_breed = [_Instance_breed or self.getRandValue(self.breeds), "Breed"]
        self._Instance_age = [int(_Instance_age) or random.randint(1, 25), "Age"]
        self._Instance_color = [_Instance_color or self.getRandValue(self.colors), "Color"]
        self._Instance_condition = [_Instance_condition or self.getRandValue(self.conditions), "Condition"]

    def getRandValue(self, array):
        return array[random.randint(0, len(array) - 1)]

    def printInfo(self):    # ToDo: make this func get user choice of dog not pass it in
        print("\n")
        for field in dir(self):
            if field.startswith("_Instance_"):
                keyAndTitle = self.__getattribute__(field)
                print(f" - {keyAndTitle[1]}: {keyAndTitle[0]}")
        print("\n")

    def printNames(array):
        for index, dog in enumerate(array):
            print(f"({index + 1}): {dog._Instance_firstName[0]} {dog._Instance_lastName[0]}", sep="\n")

    def addDog(dogs):
        newDog = Dog()
        newDog.editDog()
        dogs.append(newDog)

    def removeDog(dog, array):
        array.remove(dog)

    def editDog(self):
        for field in dir(self):
            if field.startswith("_Instance_"):
                keyAndTitle = self.__getattribute__(field)
                self.__setattr__(field, [input(keyAndTitle[1] + ": "), keyAndTitle[1]])

    def default():
        print("Invalid Choice!")
